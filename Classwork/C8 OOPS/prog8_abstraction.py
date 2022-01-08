class Demo():
    def __init__(self):
        self.public = 'pub'
        self._protected = 'prot'
        self.__private = 'priv'

    def __privateMethod(self):
        print(self.__private)

    def _protectedMethod(self):
        print(self._protected)

    def publicMethod(self):
        #self.__privateMethod()
        print(self.public)

class Derived(Demo):
    def __init__(self):
        Demo.__init__(self)
        #self._protectedMethod()
        pass

def main():
    D = Demo()
    D.publicMethod()
    D._protectedMethod()
    #D.__privateMethod()

    Dr = Derived()
    Dr._protectedMethod()

if __name__ == '__main__':
    main()