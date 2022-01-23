import threading as MT
AMOUNT = 1000

def counter (func, lock):
    func(lock)
def credit(lock)->None:
    amt = int(input('Enter amt to Credit'))
    lock.acquire()
    global AMOUNT
    AMOUNT+=amt
    print(f'Credited Amt: {amt}')
    print(f'Balance is  : {AMOUNT}')
    lock.release()
def debit(lock)->None:
    amt = int(input('Enter amt to Debit'))
    lock.acquire()
    global AMOUNT
    if(amt > AMOUNT):
        print('Unable to withdraw')
    else:
        AMOUNT-=amt
        print(f'Withdrawn : {amt}')
        print(f'Balance is:{AMOUNT}')
    lock.release()


def main():
    lock = MT.Lock()
    T1 = MT.Thread(target = counter, args=(credit, lock))
    T2 = MT.Thread(target = counter, args=(debit, lock))
    T1.start()
    T2.start()
    T1.join()
    T2.join()

    print('ENd of main')

if __name__ == '__main__':
    main()