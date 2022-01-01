def add(no1, no2):
    return no1+no2

def main():
    print("Add App")
    int1 = input("Enter 1st Number ")
    int2 = input("Enter 2nd Number ")
    ans = add(int(int1),int(int2))
    print('addition is' , ans)

if( __name__ == '__main__'):
    main()