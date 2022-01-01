from functools import reduce
add = lambda x:x+1
add2 = lambda x,y:x+y
cond = lambda x:x%2==0
def main():
    nos = [1,2,3, 4]
    
    #Map : Transform each element
    mapObj = map(add, nos)
    print(list(mapObj))

    #Filter : COdnitional filter
    filterObj = filter(cond, nos)
    print(list(filterObj))

    #Reduce : Cumulitive addition
    redObj = reduce(add2,nos)
    print(redObj)

if(__name__ == '__main__'):
    main()