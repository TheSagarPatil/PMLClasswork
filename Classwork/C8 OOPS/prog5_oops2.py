class Demo:
    A = 10
    B = 20

    def __init__(self):
        self.c = 30
        self.d = 40

def printValuesOfInstance(INST, CLASS)->None:
    className = INST.__class__.__name__
    print('class :', className, '====')
    print('value of A ' , CLASS.A)
    print('value of B ' , CLASS.B)
    print('value of c ' , INST.c)
    print('value of d ' , INST.d)
    #print('Arguments of this methods were:', locals())
    
def main():
    
    d = Demo()
    d2 = Demo()
    printValuesOfInstance(d, Demo)
    printValuesOfInstance(d2, Demo)
    d2.c +=1
    Demo.A +=1
    printValuesOfInstance(d, Demo)
    printValuesOfInstance(d2, Demo)

if __name__ == '__main__':
    main()