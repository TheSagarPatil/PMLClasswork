input = '1'
print( isinstance(input, int) )

a = [ 1, 2, 3, 4 ]
b = [ i for i in a ]
c = a
a.append(5)
print(b)
print(c)

class a:
    def __init__(self, age):
        self.__age = age
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, val):
        self.__age = val

A = a(22)
print(A.age)
