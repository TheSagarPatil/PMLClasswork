class Base1:
    def __init__(self):
        self.a = 10
        print('Inside base1')

    def fun(self):
        print('fun of base1')

class Base2:
    def __init__(self):
        self.b = 20
        print('Inside base2')

    def gun(self):
        print('gun of base2')

    def fun(self):
        print('fun of base2')

class Derived(Base1, Base2):
    def __init__(self):
        print('inside derived')
        Base1.__init__(self)
        Base2.__init__(self)
        self.c = 30
    
    #def fun(self):
    #    print('sun of derived')

def main():
    D = Derived()
    D.fun()

if __name__ == '__main__': 
    main()

