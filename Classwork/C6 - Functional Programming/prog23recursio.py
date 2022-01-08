import sys
def display(num):
    print(num)
    if(num == 1):
        return
    else:
        return display(num-1)
def display2():
    for i in range(0,5,1):
        print(i)

def stackDisp(no):
    print(no)
    if(no < 2000):
        yield stackDisp(no+1)


#display(5)
#display2()
print(sys.getrecursionlimit())
#for i in stackDisp(1):
#    print(i)