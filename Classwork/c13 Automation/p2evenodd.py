import time as TIME
import os as OS
import multiprocessing as MP
def checkEvenOdd(x)->str:
    if(x==0):
        return 'ZERO'
    elif x%2==0:
        return 'EVEN'
    elif not x%2==0:
        return 'ODD'

def multFunc(x):
    TIME.sleep(0.5)
    res = checkEvenOdd(x)
    print(f'{OS.getpid()} {x} is {res}')

def main():
    print('single process thread app')
    startTime = TIME.time()
    
    pool = MP.Pool()
    pool.map(multFunc, range(0,100))
    print(len(pool._pool))
    pool.close()

    endtime = TIME.time()
    print(f'Performance : { endtime - startTime }')

if __name__ == '__main__':
    main()

#int ques 1/16/2022 8:34 (approx 2 hrs)