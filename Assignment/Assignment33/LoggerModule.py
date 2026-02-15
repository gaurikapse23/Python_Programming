import logging
import os

def CreateLog(logDir):
    if not os.path.exists(logDir):
        os.mkdir(logDir)

    logging.basicConfig(
        filename=os.path.join(logDir, "PlatformLog.log"),
        level=logging.INFO,
        format="%(asctime)s : %(message)s"
    )