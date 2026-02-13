import os
import shutil
import sys
from Logger import CreateLogger
import logging

def DirectoryCopyExt(src, dest, extension):
    if not os.path.isdir(src):
        logging.error("Invalid source directory")
        return

    if not os.path.exists(dest):
        os.mkdir(dest)

    for file in os.listdir(src):
        if file.endswith(extension):
            shutil.copy(os.path.join(src, file), dest)
            logging.info(f"Copied {file}")

def main():
    CreateLogger()

    if len(sys.argv) != 4:
        logging.error("Invalid arguments")
        return

    DirectoryCopyExt(sys.argv[1], sys.argv[2], sys.argv[3])

if __name__ == "__main__":
    main()