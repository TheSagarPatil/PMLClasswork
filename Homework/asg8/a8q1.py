import threading as MT
def even(n):
    return n%2==0

def getNumbers(func, flag):
    cnt = 0
    no = 0
    while cnt < 10:
        if no == 0:
            no+=1
            continue
        if(func(no) == flag):
            print(f'{MT.current_thread().name} : {no}')
            cnt+=1
        no+=1

def main():
    T1 = MT.Thread(target = getNumbers, args = (even, True), name='Even')
    T2 = MT.Thread(target = getNumbers, args = (even, False), name='Odd')
    T1.start()
    T2.start()

if __name__ == '__main__':
    main()