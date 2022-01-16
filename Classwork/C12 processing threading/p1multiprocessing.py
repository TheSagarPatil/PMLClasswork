import threading as T
import os as OS
import pandas as PD
import sys as SYS
import multiprocessing as MP
def main():
    print(f'{OS.path.dirname(SYS.executable)}')
    print('PVM Process mgmt manages this > tasklist')
    print(f'{MP.cpu_count()}')
    print(f'PID of current process : {OS.getpid()}' )
    print(f'PID of Parent  process : {OS.getppid()}')

def func2():
    print(f'PID of current process : {OS.getpid()}' )

if __name__ == '__main__':
    main()