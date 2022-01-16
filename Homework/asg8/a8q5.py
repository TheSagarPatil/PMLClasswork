import threading as MT
import multiprocessing as MP
import functools 

def print50():
    for i in range(1,50):
        print(f'{MT.current_thread().name} : {i}')

def print50rev():
    for i in range(51,0, -1):
        print(f'{MT.current_thread().name} : {i}')

def main():
    data = 'abcdef12345ABCD'
    P1, P2 = MP.Pool(), MP.Pool()
    T1 = MT.Thread(name='for', target=print50, args=())
    T2 = MT.Thread(name='bkw', target=print50rev, args=())
    
    threads = [T1,T2]
    for t in threads:
        t.start()

    for t in threads:
        t.join()
    print('End of main')


if __name__ == '__main__':
    main()