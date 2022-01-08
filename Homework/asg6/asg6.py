class BookStore():
    numOfBooks = 0
    def __init__ (self,  name, author):
        self.name = name
        self.author = author
        BookStore.numOfBooks += 1

    
    def display(self):
        print(self.name, self.author, self.numOfBooks)

class BankAccount():
    __INTEREST = 4
    amount = 0
    accounts = 0
    def __init__(self, name, amount):
        self.name = name
        self.amount =  0 
        self.deposite(amount)
        BankAccount.accounts += 1

    def displayDetails(self):
        print('Name : ', self.name)
        print('Amnt : ', self.amount)
        print('-------------')
        print('Bank Details :',BankAccount.amount, BankAccount.accounts)
    def deposite(self, amount):
        self.amount += amount
        BankAccount.amount += amount
    def withdraw(self, amount):
        self.amount -= amount
        BankAccount.amount -= amount
    def calculateInterest(self):
        return (BankAccount.__INTEREST * 1 * self.amount)//100 

class Numbers():
    pass

class Arithmatic():
    def __init__(self, value):
        Numbers.__init__(self)
        self.iValue = value
    def getPerfectNumberMessage(self):
        isPerfect = self.checkPerfect()
        if (isPerfect):
            return 'Given number {} is perfect'.format(self.iValue)
        else:
            if(self.iValue <=5 ):
                return 'Perfect number is always greater than 5'
            return 'Given number {} is not perfect'.format(self.iValue)
            
    def checkPrime(self):
        isPrime = True
        if(self.iValue == 0 or self.iValue == 1 or self.iValue == 2 ):
            isPrime = False
            return isPrime
        for i in range(3, (self.iValue // 2) + 1 , 1):
            if ( self.iValue % i == 0):
                isPrime = False
                break
        return isPrime

    def checkPerfect(self):
        sumOfFactors = self.getSumFactors()
        if( sumOfFactors > 0):
            return self.iValue == (1 + sumOfFactors)
        else:
            return False

    def getFactors(self)->list:
        factors = list()
        if(self.iValue == 0 or self.iValue == 1 or self.iValue == 2 ):
            return factors #return empty list if no is 0,1,2
        for i in range(2, (self.iValue //2 )+1, 1):
            if(self.iValue % i ==0):
                factors.append(i)
        return factors

    def getSumFactors(self):
        return sum(self.getFactors())

    


    
    
def main():
    Book1 = BookStore('Linux', 'Robert Love')
    Book1.display()
    Book2 = BookStore('C Prog', 'Denis Richie')
    Book2.display()

    BankA1 = BankAccount('Sagar', 2000)
    BankA2 = BankAccount('Sagar 2 ', 3000)
    BankA1.displayDetails()
    BankA2.displayDetails()
    BankA2.deposite(1000)
    BankA2.withdraw(500)
    BankA2.displayDetails()

    A1 = Arithmatic(17)
    A2 = Arithmatic(18)
    A6 = Arithmatic(6)
    print(A1.checkPrime(), A1.getFactors(), A1.getSumFactors(), A1.checkPerfect(), A1.getPerfectNumberMessage() )
    print(A2.checkPrime(), A2.getFactors(), A2.getSumFactors(), A2.checkPerfect(), A2.getPerfectNumberMessage() )
    print(A6.checkPrime(), A6.getFactors(), A6.getSumFactors(), A6.checkPerfect(), A6.getPerfectNumberMessage() )
if __name__ == '__main__' :
    main()
