from functools import wraps 
def repeatCapitalizedNames(times=1):
    def capitalizedMethods(func):
        wraps(func)
        def func_wrapper(*args):
            return (func(*args).upper() + '\n') *times
        return func_wrapper
    return capitalizedMethods

@repeatCapitalizedNames()
def printName( name):
    return "my name is {}".format(name)

class Demo:
    #class variable
    clsVar = 5
    def __init__(self, ):
        print('Demo INITIATED')
        #instance Variable
        self.B = 20
        print(self.printName('sagar'))

    def __del__(self):
        print('Demo instance DESTROYED')   

    def InstanceMethod(self):
        #No Decorator, self
        print('inside instanceMethod')
        print(self.B)
        print(self.clsVar)

    @repeatCapitalizedNames()
    def printName(self, name):
        return "my name is {}".format(name)

    @classmethod
    def ClassMethod(cls):
        print(cls.clsVar)
        #Decorator, class, 
        print('Inside Class Method')

    @staticmethod
    def StaticMethod():
        #decorator, no class/inst param
        print('Inside Static Method')

def main():
    D = Demo()
    #GOOD PRACTICE
    D.InstanceMethod()
    Demo.ClassMethod()
    Demo.StaticMethod()

    D = None
    print('End of lifecycle')

    """#BAD PRACTICE
    D.InstanceMethod()
    Demo.ClassMethod()
    Demo.StaticMethod()"""
    

if __name__ == '__main__':
    main()
    print('End of Application')