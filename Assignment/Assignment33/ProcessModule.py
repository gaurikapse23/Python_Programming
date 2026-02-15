import psutil
import logging
from datetime import datetime

def ProcessMonitor():
    processList = []

    for proc in psutil.process_iter(['pid', 'name']):
        try:
            info = proc.info
            p = psutil.Process(info['pid'])

            processList.append({
                "name": info['name'],
                "pid": info['pid'],
                "cpu": p.cpu_percent(interval=0.1),
                "rss": p.memory_info().rss,
                "vms": p.memory_info().vms,
                "mem_per": p.memory_percent(),
                "threads": p.num_threads(),
                "files": len(p.open_files())
            })

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            logging.info("Access Denied")

    return processList


def LogProcesses(processes):
    for p in processes:
        logging.info(
            f"Process:{p['name']} | PID:{p['pid']} | CPU:{p['cpu']}% | "
            f"RSS:{p['rss']} | Threads:{p['threads']} | "
            f"OpenFiles:{p['files']}"
        )


def TopMemoryProcesses(processes):
    return sorted(processes, key=lambda x: x['rss'], reverse=True)[:10]