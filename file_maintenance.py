import os
import shutil
from datetime import datetime

def organize_files_by_extension(target_folder):
    log_file = os.path.join(target_folder, f"file_maintenance_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
    with open(log_file, "w") as log:
        for item in os.listdir(target_folder):
            item_path = os.path.join(target_folder, item)
            if os.path.isfile(item_path):
                ext = os.path.splitext(item)[1][1:].lower() or "no_extension"
                ext_folder = os.path.join(target_folder, ext)
                if not os.path.exists(ext_folder):
                    os.mkdir(ext_folder)
                    log.write(f"Created folder: {ext_folder}\n")
                shutil.move(item_path, os.path.join(ext_folder, item))
                log.write(f"Moved: {item} → {ext_folder}\n")
        log.write("File organization complete.\n")

if __name__ == "__main__":
    target_folder = os.path.expanduser("~/Desktop")  # Change this path as needed
    organize_files_by_extension(target_folder)
    print("File organization complete. Check the log file in your target folder for details.")
