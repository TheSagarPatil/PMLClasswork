from  functools import reduce
lambdaPowerOfTwo = lambda x:x**2

Q1List = [4,6]

print(list(map(lambdaPowerOfTwo, Q1List)))

#NUmbers which are greater or equal to 70 AND less/equal to 90
filterLessEq70GAndreatEq90 = lambda x:x>= 70 and x<=90
Q3List = [4,34,36,70,68,24,89,23,86,90,45,70]
print('Q3', list(filter(filterLessEq70GAndreatEq90, Q3List)))

Q4List = [5,2,3,4,3,4,1,2,8,0]
#Filter : Even odd
#Map : Square
#Reduce : Sum

FILTER_evenOdd = lambda x: x%2 ==0
MAP_square = lambda x : x**2
REDUCE_sum = lambda x,y:x+y

print(list(filter(FILTER_evenOdd, Q4List)))
print(list(map(MAP_square, Q4List)))
print(reduce(REDUCE_sum, Q4List))

Q5List = [2,30,11,10,17,23,31,77]
#filter prime numbers
#map mul by 2
#reduce max
isPrime = lambda x: all(x%(n) != 0 for n in range(2,x,1))
getMax = lambda x,y: max(x,y)
mulByTwo = lambda x:x*2
fOut = list(filter(isPrime, Q5List))
print(fOut)
mOut = list(map(mulByTwo, fOut))
print(mOut)
print(reduce(getMax, mOut))