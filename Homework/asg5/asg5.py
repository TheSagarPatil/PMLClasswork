"""
Class Demo 
instance no1, no2
instance moethods Fun Gun

"""

class Demo:
    Value = 0
    def __init__(self, no1, no2) -> None:
        self.no1 = no1
        self.no2 = no2

    def Fun(self):
        print(self.Value)

    def Gun(self):
        print(self.no1, self.no2)

def main():
    O1 = Demo(11,21)
    O2 = Demo(51,101)

    O1.Fun()
    O1.Gun()
    O2.Fun()
    O2.Gun()

if ( __name__ == '__main__'):
    main()