def maximum (value1, value2):
    if(value1 > value2):
        return value1
    elif(value2 > value1):
        return value2
    else:
        return 0

def main():
    n1 = int(input("Enter first number"))
    n2 = int(input("Enter second number"))

    print("Max number of the two given nums is", maximum(n1,n2))


if(__name__ == '__main__'):
    main()