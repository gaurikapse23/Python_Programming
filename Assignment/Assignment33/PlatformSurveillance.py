import sys
import time
import logging
from LoggerModule import CreateLog
from ProcessModule import ProcessMonitor, LogProcesses, TopMemoryProcesses
from MailModule import SendMail

def main():
    if len(sys.argv) != 4:
        print("Usage: PlatformSurveillance.py <LogDir> <Email> <Interval>")
        return

    logDir = sys.argv[1]
    email = sys.argv[2]
    interval = int(sys.argv[3]) * 60

    CreateLog(logDir)

    while True:
        processes = ProcessMonitor()
        LogProcesses(processes)

        topMem = TopMemoryProcesses(processes)

        summary = f"""
        Total Processes: {len(processes)}
        Top Memory Processes:
        """

        for p in topMem:
            summary += f"\n{p['name']} - {p['rss']}"

        SendMail(
            email,
            summary,
            f"{logDir}/PlatformLog.log"
        )

        time.sleep(interval)

if __name__ == "__main__":
    main()