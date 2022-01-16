import threading as MT
import os as OS
import pandas as PD
import sys as SYS
import multiprocessing as MP
"""When to MP or MT

"""
def fun(n):
    print(f'FUN : PID is {OS.getpid()}')
    print(f'FUN : PPID is {OS.getppid()}')
    print(f'{MT.current_thread().name}')
    for i in range(n):
        print(f'fun {i}')

def gun(n):
    print(f'GUN : PID is {OS.getpid()}')
    print(f'GUN : PPID is {OS.getppid()}')
    print(f'{MT.current_thread().name}')
    for i in range(n):
        print(f'gun {i}')

def main():
    X = 5
    print(f'Main : PID is {OS.getpid()}')
    T1 = MT.Thread(target=fun, args = (X,), name='FUN_THREAD')
    T2 = MT.Thread(target=gun, args = (X,), name='GUN_THREAD')
    T1.start()
    T2.start()

    #parent should wait for child to finish
    T1.join()
    T2.join()
    print('End of main')

if __name__ == '__main__':
    main()