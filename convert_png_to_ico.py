# convert_png_to_ico.py
# ```bash
# pip install pillow```
import os
from PIL import Image

# 🔧 Configuration
SOURCE_DIR = r"path\to\file"
ICON_SIZES = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]  # adjust as needed

def convert_png_to_ico(png_path):
    ico_path = os.path.splitext(png_path)[0] + ".ico"
    try:
        with Image.open(png_path) as img:
            if img.mode != "RGBA":
                img = img.convert("RGBA")
            img.save(ico_path, format="ICO", sizes=ICON_SIZES)
            print(f"✅ Converted: {png_path} -> {ico_path}")
    except Exception as e:
        print(f"❌ Failed to convert {png_path}: {e}")

def convert_all_pngs(root_dir):
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.lower().endswith(".png"):
                full_path = os.path.join(root, file)
                convert_png_to_ico(full_path)

if __name__ == "__main__":
    print("🔄 Starting PNG to ICO conversion...")
    convert_all_pngs(SOURCE_DIR)
    print("✅ Done.")
