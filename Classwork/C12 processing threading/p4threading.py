import os as OS
import multiprocessing as MP
import threading as MT
import time as T
"""When to MP or MT"""
def getSquare(no):
    #print(f'PID : {OS.getpid()}')
    return no * no
def getCube(no):
    return no * no * no
def main():
    print(f'{MP.cpu_count()}')

    data = [5,3,1,4,8,2,36,7,0,9]
    result = list()
    result2 = list()
    t1 = T.time()
    for i in data:
        result2.append(getSquare(i))
    print(f'{result2} counted in {t1-T.time()}')
    t2 = T.time()
    P = MP.Pool()
    result = P.map(getSquare, data)
    print(f'{result2} counted in {t2-T.time()}')


    #parallel programming


if __name__ == '__main__':
    main()