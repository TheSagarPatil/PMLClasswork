class Arithmetic:
    def  __init__(self, a,b):
        print('inside Constructor')
        self.no1 = a
        self.no2 = b
        
    def Addition(self):
        ans=self.no1 + self.no2
        return ans

def main():
    print("Nta Fust Numba")
    x = int(input())
    print("Nta Sekon Numba")
    y = int(input())

    A = Arithmetic(x,y)
    print(A.Addition())

if __name__ == '__main__':
    main()
