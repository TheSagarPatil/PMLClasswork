import threading as MT
import multiprocessing as MP
import functools 

def getCount(data, func):
    cnt = 0
    for char in data:
        if(func(char)):
            cnt+=1
    print(f'{MT.current_thread().name} : {cnt}')
    return cnt

def main():
    data = 'abcdef12345ABCD'
    P1, P2 = MP.Pool(), MP.Pool()
    T1 = MT.Thread(name='upper', target=getCount, args=(data, str.isupper))
    T2 = MT.Thread(name='lower', target=getCount, args=(data, str.islower))
    T3 = MT.Thread(name='digit', target=getCount, args=(data, str.isnumeric))
    threads = [T1,T2,T3]
    for t in threads:
        t.start()

    for t in threads:
        t.join()
    print('End of main')


if __name__ == '__main__':
    main()