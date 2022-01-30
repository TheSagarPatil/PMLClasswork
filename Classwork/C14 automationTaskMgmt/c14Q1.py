
"""
Get details of running processes and show them
"""
import psutil as PSU
import json as JSON

def getProcessDetail() -> list[dict]:
    processes = []
    for proc in PSU.process_iter():
        try:
            _proc = proc.as_dict(attrs=[ 'pid', 'name', 'username' ])
            _proc['usage'] = proc.memory_info().vms // (1024 ** 2)
            processes.append(_proc)
        except (PSU.NoSuchProcess, PSU.AccessDenied, PSU.ZombieProcess):
            print('Error occured in collecting data')
        finally:
            sortedProcessses = sorted(processes, key= lambda i:i['usage'], reverse=True)
    return sortedProcessses

def killProcess(processes :dict, processName :str):
    similarProc : list[dict] = []
    for proc in processes:
        if(processName in proc['name'] ):
            similarProc.append(proc)
    if (len(similarProc)>0):
        for proc in similarProc:
            print(f'{proc["name"]} is found')
    else:
        print(f'No processes found')

def main() -> None:
    processes = getProcessDetail()
    fileObj = open("H:\\DIR_EXPT\\att\\log.json","w")
    JSON.dump(processes, fileObj, indent=2)
    fileObj.close()
    print('Top 10 Processes', JSON.dumps(processes[:10], indent = 2))
    killProcess(processes, 'notepad.exe')

if __name__ == '__main__':
    main()
