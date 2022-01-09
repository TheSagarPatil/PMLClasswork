class RecursionDemo():
    def __init__(self, num):
        self.num = num
        print()
        
        print(f"""Given number is {self.num}
its sum of numbers is {self.getSum()}
        """)
    def getSum(self):
        self.n = self.num
        sum = 0
        sum = self.getSummession(self.num, 0, 0)
        return sum

    @staticmethod
    def display5StarPattern(num):
        if(num !=0 ):
            print('*\t', end='')
            RecursionDemo.display5StarPattern(num-1)

    @staticmethod
    def displayFirst5(limit, num=1 ):
        if(num <= limit):
            print(num,'\t', end='')
            RecursionDemo.displayFirst5(limit, num+1)
    @staticmethod
    def displayFirst5Reverse(limit):
        if(limit > 0):
            print(limit, '\t', end='')
            RecursionDemo.displayFirst5Reverse(limit - 1)


    @staticmethod
    def getSummession(num, sum, rem):
        if num != 0:
            rem = num % 10
            num = num //10
            sum = rem + RecursionDemo.getSummession(num, sum, rem)
            return sum
        else:
            return 0

    @staticmethod
    def getSumession(num):
        sum=0
        while(num!=0):
            sum+= num%10
            num//=10
        return sum

    def getFactorial(self, num):
        if(num > 1):
            return num * self.getFactorial(num-1)
        else:
            return 1
        
def main():
    INPUT = 5
    print(f"""Display Sum of numbers for input 879:-> 24""")
    R = RecursionDemo(879)
    print(f"""Display Following pattern for input {INPUT}: * * * * * """)
    R.display5StarPattern(INPUT)
    print('')
    print(f"""Display Following pattern for input {INPUT}: 1 2 3 4 5 """)
    R.displayFirst5(INPUT)
    print('')
    print(f"""Display Following pattern for input {INPUT}: 5 4 3 2 1 """)
    R.displayFirst5Reverse(INPUT)
    print('')
    print(f"""Display Factorial : {INPUT} -> 120  """)
    print(f"Factorial of {INPUT} is {R.getFactorial(5)}")

if __name__ == '__main__':
    main()