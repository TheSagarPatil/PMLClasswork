import threading as MT
import multiprocessing as MP
import functools 
def isEven(n):
    return n%2==0
def isOdd(n):
    return not isEven(n)
def getNumbers(numbers, func):
    l = list()
    for n in numbers:
        if(func(n)):
            l.append(n)

def main():
    data = [1,2,3,4,5,6,7,8,9,0]
    P1, P2 = MP.Pool(), MP.Pool()
    T1 = MT.Thread(name='Even', target=getNumbers, args=(data, isEven))
    T2 = MT.Thread(name='Odd', target=getNumbers, args=(data, isOdd))
    T1.start()
    T2.start()

if __name__ == '__main__':
    main()