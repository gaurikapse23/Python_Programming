import os
import sys
from Logger import CreateLogger
import logging

def DirectoryRename(dirName, oldExt, newExt):
    if not os.path.isdir(dirName):
        logging.error("Invalid directory")
        return

    for file in os.listdir(dirName):
        if file.endswith(oldExt):
            oldPath = os.path.join(dirName, file)
            newFile = file.replace(oldExt, newExt)
            newPath = os.path.join(dirName, newFile)
            os.rename(oldPath, newPath)
            logging.info(f"Renamed {file} to {newFile}")

def main():
    CreateLogger()

    if len(sys.argv) != 4:
        logging.error("Invalid arguments")
        return

    DirectoryRename(sys.argv[1], sys.argv[2], sys.argv[3])

if __name__ == "__main__":
    main()