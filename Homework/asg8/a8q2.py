import threading as MT

def getFactors(n, evFlag=None):
    factors, evnFactors, oddFactors = list(), list(), list()
    for i in range(1,n//2):
        if(n%i == 0):
            if evFlag == None :
                factors.append(i)
            if i%2 == 0:
                evnFactors.append(i)
            if not i%2 == 0:
                oddFactors.append(i)
    returnee = {
        None : factors,
        True : evnFactors,
        False: oddFactors
    }
    _returnee = returnee[evFlag]
    print(f'{MT.current_thread().name} : {_returnee}')
    return _returnee
    
def main():
    T1 = MT.Thread(target = getFactors, args = (36, True), name='EvenFactors')
    T2 = MT.Thread(target = getFactors, args = (36, False), name='OddFactors')
    T1.start()
    T2.start()
    T1.join()
    T2.join()
    print(f'End of Main')

if __name__ == '__main__':
    main()