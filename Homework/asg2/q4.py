def getFactors(n):
    factorList = []
    for i in range(2, n):
        m = n%i
        if(m == 0):
            factorList.append(i)
    return factorList

def getSumOfFactors(n):
    factorList = getFactors(n)
    sum=0
    for f in factorList:
        sum+=f
    return sum

print(getSumOfFactors(10))

