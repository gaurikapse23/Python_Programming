import os
import sys
from Logger import CreateLogger
import logging

def DirectoryFileSearch(dirName, extension):
    if not os.path.isdir(dirName):
        logging.error("Invalid directory")
        return

    for file in os.listdir(dirName):
        if file.endswith(extension):
            logging.info(file)

def main():
    CreateLogger()

    if len(sys.argv) != 3:
        logging.error("Invalid arguments")
        return

    DirectoryFileSearch(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()