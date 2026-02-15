import os
import sys
import zipfile
import time
from datetime import datetime

LOG_DIR = "Logs"
HISTORY_FILE = "History.txt"
EXCLUDE_EXT = [".tmp", ".log", ".exe"]

# -------------------------------------------------
def create_log():
    if not os.path.exists(LOG_DIR):
        os.mkdir(LOG_DIR)
    return open(os.path.join(LOG_DIR, "BackupLog.txt"), "a")

# -------------------------------------------------
def should_exclude(file):
    return any(file.endswith(ext) for ext in EXCLUDE_EXT)

# -------------------------------------------------
def backup(source):
    log = create_log()
    start_time = datetime.now()

    zip_name = f"Backup_{start_time.strftime('%Y%m%d_%H%M%S')}.zip"
    file_count = 0

    try:
        with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(source):
                for file in files:
                    if should_exclude(file):
                        continue
                    path = os.path.join(root, file)
                    zipf.write(path)
                    file_count += 1

        log.write(f"\nBackup Started : {start_time}\n")
        log.write(f"Files Copied   : {file_count}\n")
        log.write(f"Zip File       : {zip_name}\n")

        with open(HISTORY_FILE, "a") as h:
            h.write(f"{start_time} | Files: {file_count} | Zip: {zip_name}\n")

    except Exception as e:
        log.write(f"Error : {e}\n")

    log.close()

# -------------------------------------------------
def restore(zip_name, destination):
    with zipfile.ZipFile(zip_name, 'r') as zipf:
        zipf.extractall(destination)

# -------------------------------------------------
def show_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE) as f:
            print(f.read())
    else:
        print("No history found")

# -------------------------------------------------
def main():
    if len(sys.argv) < 2:
        print("Invalid Arguments")
        return

    if sys.argv[1] == "--restore":
        restore(sys.argv[2], sys.argv[3])

    elif sys.argv[1] == "--history":
        show_history()

    else:
        if not os.path.isdir(sys.argv[1]):
            print("Invalid directory")
            return
        backup(sys.argv[1])

# -------------------------------------------------
if __name__ == "__main__":
    main()