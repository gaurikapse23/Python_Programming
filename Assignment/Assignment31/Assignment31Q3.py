import os
import shutil
import sys
from Logger import CreateLogger
import logging

def DirectoryCopy(src, dest):
    if not os.path.isdir(src):
        logging.error("Source directory invalid")
        return

    if not os.path.exists(dest):
        os.mkdir(dest)

    for file in os.listdir(src):
        shutil.copy(os.path.join(src, file), dest)
        logging.info(f"Copied {file}")

def main():
    CreateLogger()

    if len(sys.argv) != 3:
        logging.error("Invalid arguments")
        return

    DirectoryCopy(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()