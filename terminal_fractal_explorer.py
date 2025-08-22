#!/usr/bin/env python3
# Terminal Fractal Explorer: Mandelbrot + Julia (color, pan, zoom, save, record)
# No deps required. Optional: Pillow for saving PNGs.
# Author: Russell Henderson

import os, sys, time, math, shutil, threading
from dataclasses import dataclass
from typing import Tuple, Optional

# ---------- Cross-platform keyboard input ----------
IS_WIN = os.name == "nt"
if IS_WIN:
    import msvcrt
else:
    import termios, tty, select

def get_key_nonblocking(timeout=0.0) -> Optional[str]:
    if IS_WIN:
        start = time.time()
        while time.time() - start < timeout:
            if msvcrt.kbhit():
                ch = msvcrt.getwch()
                if ch in ("\x00", "\xe0"):  # arrows as two-key sequence
                    ch2 = msvcrt.getwch()
                    return {"H":"UP", "P":"DOWN", "K":"LEFT", "M":"RIGHT"}.get(ch2, None)
                if ch == "\x1b":
                    return "ESC"
                return ch
            time.sleep(0.005)
        return None
    else:
        dr, _, _ = select.select([sys.stdin], [], [], timeout)
        if dr:
            ch = sys.stdin.read(1)
            if ch == "\x1b":
                # Possibly an escape sequence
                if select.select([sys.stdin], [], [], 0.0005)[0]:
                    seq = sys.stdin.read(2)
                    mapping = {"[A":"UP", "[B":"DOWN", "[D":"LEFT", "[C":"RIGHT"}
                    return mapping.get(seq, "ESC")
                return "ESC"
            return ch
        return None

class RawTTY:
    def __enter__(self):
        if not IS_WIN:
            self.fd = sys.stdin.fileno()
            self.old = termios.tcgetattr(self.fd)
            tty.setcbreak(self.fd)
        return self
    def __exit__(self, *exc):
        if not IS_WIN:
            termios.tcsetattr(self.fd, termios.TCSADRAIN, self.old)

# ---------- ANSI helpers ----------
CSI = "\x1b["
def hide_cursor():   sys.stdout.write(CSI + "?25l")
def show_cursor():   sys.stdout.write(CSI + "?25h")
def clear_screen():  sys.stdout.write(CSI + "2J" + CSI + "H")
def move_home():     sys.stdout.write(CSI + "H")
def set_fg_rgb(r,g,b): sys.stdout.write(f"\x1b[38;2;{r};{g};{b}m")
def set_bg_rgb(r,g,b): sys.stdout.write(f"\x1b[48;2;{r};{g};{b}m")
def reset_color():   sys.stdout.write("\x1b[0m")

# Use half-block "▄" so each cell represents two vertical pixels
HALF_BLOCK = "▄"

# ---------- Color palettes ----------
def palette_smooth(t: float) -> Tuple[int,int,int]:
    # Smooth cyclic palette using cosine ramps
    a, b, c, d = 0.5, 0.5, 1.0, 0.0
    r = int(255 * (a + b * math.cos(2*math.pi*(c*t + d    ))))
    g = int(255 * (a + b * math.cos(2*math.pi*(c*t + d+1/3))))
    b_ = int(255 * (a + b * math.cos(2*math.pi*(c*t + d+2/3))))
    return max(0,r), max(0,g), max(0,b_)

def palette_fire(t: float) -> Tuple[int,int,int]:
    # Black -> red -> yellow -> white
    x = max(0.0, min(1.0, t))
    r = int(255 * min(1.0, 3*x))
    g = int(255 * min(1.0, max(0.0, 3*x - 1)))
    b = int(255 * min(1.0, max(0.0, 3*x - 2)))
    return r, g, b

def palette_ice(t: float) -> Tuple[int,int,int]:
    x = max(0, min(1, t))
    r = int(255 * x*0.2)
    g = int(255 * (0.3 + 0.6*x))
    b = int(255 * (0.5 + 0.5*x))
    return r, g, b

PALETTES = [palette_smooth, palette_fire, palette_ice]
PALETTE_NAMES = ["smooth", "fire", "ice"]

# ---------- Fractal math ----------
def mandelbrot(c: complex, max_iter: int) -> float:
    z = 0+0j
    for n in range(max_iter):
        z = z*z + c
        if (z.real*z.real + z.imag*z.imag) > 4.0:
            # Smooth escape time
            mod = abs(z)
            return n + 1 - math.log(math.log(mod, 2), 2)
    return float(max_iter)

def julia(z: complex, c: complex, max_iter: int) -> float:
    for n in range(max_iter):
        z = z*z + c
        if (z.real*z.real + z.imag*z.imag) > 4.0:
            mod = abs(z)
            return n + 1 - math.log(math.log(mod, 2), 2)
    return float(max_iter)

# ---------- Renderer ----------
@dataclass
class View:
    cx: float = -0.5      # Center x
    cy: float = 0.0       # Center y
    scale: float = 3.0    # Width of view in complex plane
    max_iter: int = 200
    julia_mode: bool = False
    julia_c: complex = complex(-0.70176, -0.3842)
    palette_idx: int = 0

def map_screen_to_complex(x, y, cols, rows, view: View) -> complex:
    # Each text cell draws two vertical pixels, so effective rows*2
    aspect = cols / (rows*2)
    width = view.scale
    height = width / aspect
    re = view.cx + (x / cols - 0.5) * width
    im = view.cy - (y / (rows*2) - 0.5) * height
    return complex(re, im)

def render_frame(view: View, cols: int, rows: int):
    # Precompute two-pixel tall cells
    pal = PALETTES[view.palette_idx]
    buf_lines = []
    for y in range(rows):  # each row represents two vertical samples: top and bottom
        line = []
        for x in range(cols):
            # top and bottom sample points
            z_top  = map_screen_to_complex(x, 2*y,   cols, rows, view)
            z_bot  = map_screen_to_complex(x, 2*y+1, cols, rows, view)
            if view.julia_mode:
                it_top = julia(z_top, view.julia_c, view.max_iter)
                it_bot = julia(z_bot, view.julia_c, view.max_iter)
            else:
                it_top = mandelbrot(z_top, view.max_iter)
                it_bot = mandelbrot(z_bot, view.max_iter)

            # Normalize t for color
            def color_for(it):
                if it >= view.max_iter:
                    return (0,0,0)
                t = it / view.max_iter
                return pal(t)
            rt, gt, bt = color_for(it_top)
            rb, gb, bb = color_for(it_bot)

            # Foreground = top pixel color, Background = bottom pixel color
            set_fg = f"\x1b[38;2;{rt};{gt};{bt}m"
            set_bg = f"\x1b[48;2;{rb};{gb};{bb}m"
            line.append(set_fg + set_bg + HALF_BLOCK)
        buf_lines.append("".join(line) + "\x1b[0m")
    return "\n".join(buf_lines)

# ---------- Optional PNG saving ----------
def try_save_png(pixels, width, height, path):
    try:
        from PIL import Image
    except Exception:
        return False, "Install Pillow for PNG saving: pip install pillow"
    img = Image.new("RGB", (width, height))
    img.putdata(pixels)
    img.save(path)
    return True, path

def current_pixels(view: View, cols: int, rows: int):
    # Generate raw pixel array (2*rows tall)
    pal = PALETTES[view.palette_idx]
    height = rows*2
    out = []
    for y in range(height):
        for x in range(cols):
            z = map_screen_to_complex(x, y, cols, rows, view)
            it = julia(z, view.julia_c, view.max_iter) if view.julia_mode else mandelbrot(z, view.max_iter)
            if it >= view.max_iter:
                out.append((0,0,0))
            else:
                out.append(pal(it/view.max_iter))
    return out, cols, height

# ---------- Main app ----------
def clamp(v,a,b): return a if v<a else b if v>b else v

def main():
    view = View()
    # Initial size
    cols, rows = shutil.get_terminal_size((100, 40))
    rows = max(12, rows - 2)      # keep some margin
    cols = max(60, cols)

    info = ""
    recording = False

    # Raw TTY on Unix for real-time keys
    with RawTTY():
        try:
            hide_cursor()
            clear_screen()
            last_draw = 0
            while True:
                now = time.time()
                # Draw at most 30 fps to avoid spam
                if now - last_draw > 1/30:
                    move_home()
                    sys.stdout.write(render_frame(view, cols, rows))
                    sys.stdout.write("\n")
                    sys.stdout.write(
                        f"Mode: {'Julia' if view.julia_mode else 'Mandelbrot'} | "
                        f"Iter: {view.max_iter} | "
                        f"Center: ({view.cx:.6f}, {view.cy:.6f}) | "
                        f"Scale: {view.scale:.6f} | "
                        f"Palette: {PALETTE_NAMES[view.palette_idx]} | "
                        f"[Arrows] move  [=/-] zoom  [[]/]] iters  j toggle  p palette  s save  r record  0 reset  q quit\n"
                    )
                    if info:
                        sys.stdout.write(info + "\n")
                        info = ""
                    sys.stdout.flush()
                    last_draw = now

                # Handle input
                key = get_key_nonblocking(timeout=0.01)
                if not key:
                    continue

                step = view.scale * 0.05
                zoom_factor = 0.85

                if key in ("q", "Q", "ESC"):
                    break
                elif key == "LEFT":
                    view.cx -= step
                elif key == "RIGHT":
                    view.cx += step
                elif key == "UP":
                    view.cy += step
                elif key == "DOWN":
                    view.cy -= step
                elif key == "=":
                    view.scale *= zoom_factor
                    view.max_iter = int(view.max_iter * 1.02)  # gently raise detail as we zoom
                elif key == "-":
                    view.scale /= zoom_factor
                    view.max_iter = max(50, int(view.max_iter / 1.02))
                elif key == "[":
                    view.max_iter = max(20, view.max_iter - 10)
                elif key == "]":
                    view.max_iter = min(5000, view.max_iter + 10)
                elif key in ("p","P"):
                    view.palette_idx = (view.palette_idx + 1) % len(PALETTES)
                elif key in ("j","J"):
                    view.julia_mode = not view.julia_mode
                    info = f"Toggled to {'Julia' if view.julia_mode else 'Mandelbrot'}"
                elif key == "0":
                    view = View()  # reset
                    info = "View reset"
                elif key in ("s","S"):
                    pixels, w, h = current_pixels(view, cols, rows)
                    path = time.strftime("fractal_%Y%m%d-%H%M%S.png")
                    ok, msg = try_save_png(pixels, w, h, path)
                    info = f"Saved {msg}" if ok else msg
                elif key in ("r","R"):
                    # Record 40 frames zoom-in and save as PNG sequence
                    try:
                        from PIL import Image  # check before starting
                    except Exception:
                        info = "Install Pillow for recording: pip install pillow"
                        continue
                    if recording:
                        info = "Already recording"
                        continue
                    recording = True
                    def record_seq():
                        nonlocal recording, info
                        base_scale = view.scale
                        base_iter  = view.max_iter
                        frames = 40
                        for i in range(frames):
                            view.scale *= 0.92
                            view.max_iter = min(8000, int(view.max_iter*1.03))
                            pixels, w, h = current_pixels(view, cols, rows)
                            name = f"fractal_rec_{i:03}.png"
                            try_save_png(pixels, w, h, name)
                        info = f"Recorded {frames} PNG frames (fractal_rec_###.png)"
                        # restore a reasonable iteration
                        view.max_iter = base_iter
                        recording = False
                    threading.Thread(target=record_seq, daemon=True).start()
                # Resize handling
                new_cols, new_rows = shutil.get_terminal_size((100, 40))
                new_rows = max(12, new_rows - 2)
                new_cols = max(60, new_cols)
                if new_cols != cols or new_rows != rows:
                    cols, rows = new_cols, new_rows
                    clear_screen()

        finally:
            reset_color()
            show_cursor()
            sys.stdout.flush()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        reset_color()
        show_cursor()
        print()
