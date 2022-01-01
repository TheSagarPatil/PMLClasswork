import sys, time, inspect
import os as OS

debugMode = True
print("Jai Ganesh")
#START printInfo()
def printPerformance(functionName, startTime):
    if(debugMode):
        end = time.time()
        #print(functionName, 'took', startTime-end, 'ms')
        print(inspect.stack()[1][3] , 'took', startTime-end, 'ms')

def printInfo(var):
    """ 
    Input  : 
        var : variable name
    return : void 
    Prints information like type, memory size of the variable"""
    start = time.time()
    print(type(var),'\t', sys.getsizeof(var), var,'\n', '\n')
    printPerformance('printInfo', start)
    
#End printInfo definition
no = 11
name = 'Sagar'
percentage = 1.5
bigno = 1111111111111111111111111.1
complexNo = 10+5j
_set = {1,2,3}
_list = [1,2,3]
_tuple = (1,2,3)
_dict = {'a':'a1', 'b':'b1'}
expoNo = int(7E7+5)

printInfo(no)
printInfo(name)
printInfo(percentage)
printInfo(bigno)
printInfo(complexNo)
printInfo(expoNo)

no = 1111111111111111111111111

printInfo(no)
print(no + no)
printInfo(_set)
printInfo(_list)
printInfo(_dict)
printInfo(_tuple)


