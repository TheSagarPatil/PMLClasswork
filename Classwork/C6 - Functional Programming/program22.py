def addition(*iArgs):
    """
@Help
    @Author : 
        TheSagarPatil@Github
    @Description:
        Takes 2 numbers and returns addition of them
    @Parameters:
        iArgs Tuple<int> (Positional): 
    @Returns : 
            iAns <int> :   
    """
    iAns = 0
    for num in iArgs:
        iAns +=num
    return iAns
def area(iRadius):
    r = iRadius
    PI = 3.14
    return PI * r * r 
def main():
    no1 = int(input('Enter a number'))
    no2 = int(input('Enter a number'))
    #help(addition)
    print("Addition is :", addition(no1, no2))
    print("Circle Area :", area(iRadius=no1))

if(__name__ == '__main__'):
    main()