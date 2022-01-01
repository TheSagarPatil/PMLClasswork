def addition(iNo1, iNo2):
    """
@Help
    @Author : 
        TheSagarPatil@Github
    @Description:
        Takes 2 numbers and returns addition of them
    @Parameters:
        iNo1 <int> (Positional): 
        iNo2 <int> (Positional): 
    @Returns : 
            iAns <int> :   
    """
    iAns = iNo1 + iNo2
    return iAns
def area(iRadius):
    r = iRadius
    PI = 3.14
    return PI * r * r 
def main():
    no1 = int(input('Enter a number'))
    no2 = int(input('Enter a number'))
    #help(addition)
    print("Addition is :", addition(iNo1 = no2, iNo2 = no1))
    print("Circle Area :", area(iRadius=no1))

if(__name__ == '__main__'):
    main()