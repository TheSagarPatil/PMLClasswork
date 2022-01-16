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
    for i in range(n):
        print(f'fun {i}')

def gun(n):
    print(f'GUN : PID is {OS.getpid()}')
    print(f'GUN : PPID is {OS.getppid()}')
    for i in range(n):
        print(f'gun {i}')

def main():
    X = 5
    print(f'Main : PID is {OS.getpid()}')
    #OS.path.dirname(SYS.executable)
    P1 = MP.Process(target=fun, args = (X,))
    P2 = MP.Process(target=gun, args = (X,))

    T1 = MT.Thread(target=fun, args = (X,))
    T2 = MT.Thread(target=gun, args = (X,))

    P1.start()
    P2.start()

    T1.start()
    T2.start()

    #parent should wait for child to finish
    P1.join()
    P2.join()

    T1.join()
    T2.join()
    print('End of main')

if __name__ == '__main__':
    main()