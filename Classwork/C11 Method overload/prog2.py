class Base():
    def __init__ (self):
        self.i = 10
        self.j = 20
    def add(self, a):
        print('add with one param')
    def add(self, a,b):
        print('add with two param')
    def fun(self):
        print('Base fun')
    def gun(self):
        print('Base gun')

class Derived(Base):
    def __init__(self):
        self.a = 11
        self.b = 21
    def fun(self):
        print('derived fun')
    def sun(self):
        print('derived gun')

def main():
    b = Base()
    d = Derived()
    d.fun()
    d.gun()
    d.sun()

    
if __name__ == '__main__':
    main()