import psutil
import datetime
from tabulate import tabulate

def get_procsses():
    processes = []
    for p in psutil.process_iter():
        with p.oneshot():
            process_id = p.pid
            if process_id == 0:
                continue
            process_name = p.name()
            try:
                process_create_time = datetime.datetime.fromtimestamp(p.create_time())
            except OSError:
                process_create_time = datetime.datetime.fromtimestamp(psutil.boot_time())
            cpu_usage = p.cpu_percent()
            try:
                cpu_affinity = len(p.cpu_affinity())
            except psutil.AccessDenied:
                cpu_affinity = 0
            process_status = p.status()
            try:
                process_memory = p.memory_full_info().uss
            except psutil.AccessDenied:
                process_memory = 0
            try:
                process_creator_user_name = p.username()
            except psutil.AccessDenied:
                process_creator_user_name = "N/A"
        processes.append({
            'pid': process_id,
            'name': process_name,
            'create_time': process_create_time,
            'cpu_usage': cpu_usage,
            'cpu_affinity': cpu_affinity,
            'status': process_status,
            'memory': get_size(process_memory),
            'user': process_creator_user_name
        })
    return processes

def get_size(bytes):
    for i in ['', 'K', 'M', 'G', 'T', 'P', 'E']:
        if bytes < 1024:
            return f"{bytes:.2f}{i}B"
        bytes /= 1024

def print_processes(processes):
    print(tabulate(processes, headers="keys", tablefmt='github'))

print_processes(get_procsses())