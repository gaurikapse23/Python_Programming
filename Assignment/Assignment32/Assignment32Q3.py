import os
import sys
import hashlib
import time

def get_hash(file_path):
    md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for block in iter(lambda: f.read(4096), b""):
            md5.update(block)
    return md5.hexdigest()

def remove_duplicates(directory):
    size_dict = {}
    log = open("Log.txt", "w")
    log.write("Duplicate File Removal Log\n")
    log.write(f"Timestamp : {time.ctime()}\n\n")

    for folder, sub, files in os.walk(directory):
        for file in files:
            path = os.path.join(folder, file)
            size = os.path.getsize(path)

            if size in size_dict:
                file_hash = get_hash(path)
                if file_hash in size_dict[size]:
                    os.remove(path)
                    log.write(f"Removed Duplicate : {path}\n")
                else:
                    size_dict[size].add(file_hash)
            else:
                size_dict[size] = {get_hash(path)}

    log.close()

def main():
    if len(sys.argv) != 2:
        print("Usage : DirectoryDuplicateRemoval_v2.py <Directory>")
        return

    if not os.path.isdir(sys.argv[1]):
        print("Invalid directory")
        return

    remove_duplicates(sys.argv[1])

if __name__ == "__main__":
    main()