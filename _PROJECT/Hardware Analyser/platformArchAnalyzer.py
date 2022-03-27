import psutil  as PSU
import platform as PLTF
from os import *
from datetime import datetime

ESystem = {
    'undefined':'platform not identified',

    'WIN' :'Windows',
    'DWN': 'Darwin',
    'LNX': 'Linux',
}

def CPU_OS_info() -> None:
    """
    @help :
    fetches CPU and OS info
    @return : None
    """
    print(f'CPU OS Info')
    sys = PLTF.system()
    if   sys == ESystem.get('WIN') :
        return PLTF.processor()

    elif sys == ESystem.get('DWN') :
        command = '/usr/sbin/sysctl -n machdep.cpu.brand_string'
        return popen(command).read().strip()

    elif sys == ESystem.get('LNX') :
        cmd = 'cat/proc/cpuinfo'
        return popen(cmd).read().strip()

    return ESystem.get('undefined')

def get_size( bytes: int, suffix: str = 'B') -> str:
    factor = 1024
    for unit in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']:
        if bytes < factor:
            return f'{bytes :.2f} {unit}{suffix}'
        bytes /= factor

def platform_info() -> None :
    print('\n# System Information')
    uname = PLTF.uname()
    print(f'System : { uname.system }')
    print(f'Node Name : { uname.node }')
    print(f'Release : {uname.release}')
    print(f'Version : {uname.version}')
    print(f'Machine : {uname.machine}')
    print(f'Processor : {uname.processor}')

def boot_info():
    print('\n# Boot Time')
    boot_ts = PSU.boot_time()
    bt = datetime.fromtimestamp(boot_ts)
    print(f'Boottime : {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}' )

def cpu_info() -> None:
    print('\n# CPU Info')
    print(f'Physical cores: {PSU.cpu_count(logical = False)}'  )
    print(f'Total cores : {PSU.cpu_count(logical = True)} ')
    print('CPU Usage per core : ')
    cpus = PSU.cpu_percent(percpu = True)
    cpunos = len(list(enumerate(cpus)))
    sep = '-' * 8 * cpunos
    print(f'\n{sep}')
    for i, percentage in enumerate(cpus):
        print(f'  {i:<3} | ' , end = '')

    print(f'\n{sep}')
    for i, percentage in enumerate(cpus):
        print(f'{percentage :<5}% | ' , end = '')
    print(f'\n{sep}\n')

def disk_info():
    print('# Disk Info')
    partitions = PSU.disk_partitions()
    for partition in partitions:
        try :
            print('## Partition details')
            print(f'\tDevice        : { partition.device }')
            print(f'\tMountpoint    : {partition.mountpoint}')
            print(f'\tFile Sys type : {partition.fstype}')

            partition_usage = PSU.disk_usage(partition.mountpoint)
            print(f'\tTotal Size    : {get_size(partition_usage.total )}')
            print(f'\tUsed          : { get_size(partition_usage.used) }')
            print(f'\tFree          : { get_size(partition_usage.free) }')
            print(f'\tPercentage    : {partition_usage.percent}%')
            disk_io = PSU.disk_io_counters()
            print(f'\tTotal read    : {get_size(disk_io.read_bytes)}')
            print(f'\tTotal wirte   : {get_size(disk_io.write_bytes)}')

        except PermissionError:
            continue

def ram_usage() -> None:
    print('# RAM Usage')
    svMem = PSU.virtual_memory()
    print('## Virtual Memory')
    print(f'Total : { get_size(svMem.total) }')
    print(f'Available : {get_size(svMem.available)}')
    print(f'Used : {get_size(svMem.used)}')
    print(f'Percentage : {svMem.percent}%')

    swap = PSU.swap_memory()
    print('## Swap Memory')
    print(f'Total : { get_size(swap.total) }')
    print(f'Available : {get_size(swap.free)}')
    print(f'Used : {get_size(swap.used)}')
    print(f'Percentage : {swap.percent}%')

def main():
    print( CPU_OS_info() )
    disk_info()
    ram_usage()
    cpu_info()
    boot_info()
    platform_info()


if __name__ == '__main__':
    main()