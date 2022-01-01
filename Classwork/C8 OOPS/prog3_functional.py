addition= lambda x,y:x+y

def main():
    print('Enter first no')
    no1 = int(input())
    print('Enter second no')
    no2 = int(input())
    ret = addition(no1, no2)
    print(ret)

if __name__ == '__main__':
    main()