import os
import sys
import hashlib
import time

def calculate_checksum(file_path):
    hash_object = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_object.update(chunk)
        return hash_object.hexdigest()
    except Exception as e:
        return "Error"

def directory_checksum(dir_name):
    if not os.path.isdir(dir_name):
        print("Invalid Directory")
        return

    log_file = "Log.txt"
    with open(log_file, "w") as log:
        log.write("Directory Checksum Log\n")
        log.write(f"Timestamp : {time.ctime()}\n\n")

        for foldername, subfolders, filenames in os.walk(dir_name):
            for file in filenames:
                file_path = os.path.join(foldername, file)
                checksum = calculate_checksum(file_path)
                log.write(f"{file_path} : {checksum}\n")

def main():
    if len(sys.argv) != 2:
        print("Usage : DirectoryChecksum.py <DirectoryName>")
        return

    directory_checksum(sys.argv[1])

if __name__ == "__main__":
    main()