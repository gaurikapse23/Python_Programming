import os
import sys
import hashlib
import time

def checksum(file_path):
    h = hashlib.md5()
    with open(file_path, 'rb') as f:
        h.update(f.read())
    return h.hexdigest()

def delete_duplicates(dir_name):
    start_time = time.time()
    file_dict = {}
    log = open("Log.txt", "w")

    log.write("Duplicate Removal Log\n")
    log.write(f"Start Time : {time.ctime()}\n\n")

    for folder, sub, files in os.walk(dir_name):
        for file in files:
            path = os.path.join(folder, file)
            chksum = checksum(path)

            if chksum in file_dict:
                os.remove(path)
                log.write(f"Deleted Duplicate : {path}\n")
            else:
                file_dict[chksum] = path

    end_time = time.time()
    log.write(f"\nExecution Time : {end_time - start_time:.2f} seconds")
    log.close()

def main():
    if len(sys.argv) != 2:
        print("Usage : DirectoryDuplicateRemoval.py <Directory>")
        return

    delete_duplicates(sys.argv[1])

if __name__ == "__main__":
    main()