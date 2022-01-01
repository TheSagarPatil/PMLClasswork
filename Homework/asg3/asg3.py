def isPrime(no):
    _isPrime = True
    for i in range(2, no):
        if(no%i == 0):
            _isPrime = False
            break
    return _isPrime
def getSum(lst):
    sum=0
    for no in lst:
        sum+=no
    return sum
def getSumOfPrime(lst):
    sum=0
    for i in lst:
        if(isPrime(i) is  True):
            sum+=i
    return sum 
def getFrequencyOfGivenNumber(no, arr):
    length = len(arr)
    i= length //2
    j = i+1
    frequency = 0
    while(i>=0 and j<length):
        if(arr[i] == no or arr[j] ==no):
            frequency +=1
        i-=1
        j+=1
    return frequency
def getMin(arr):
    mn = arr[0]
    for no in arr:
        mn = min(mn, no)
    return mn
def getMax(arr):
    mn = arr[0]
    for no in arr:
        mn = max(mn, no)
    return mn    

def main():
    lst = [13,5,45,7,4,56,10,34,2,5,8 ]
    print('Sum of primes :', getSumOfPrime(lst))
    print('Frequency of 5:', getFrequencyOfGivenNumber(5, lst))
    print('Minimum is    :', getMin(lst))
    print('Maximum is    :', getMax(lst))
    print('Sum of list   :', getSum(lst))
if __name__ == '__main__':
    main()