import logging

def CreateLogger():
    logging.basicConfig
    (
        filename="Automation.log",
        level=logging.INFO,
        format="%(asctime)s : %(levelname)s : %(message)s"
    )