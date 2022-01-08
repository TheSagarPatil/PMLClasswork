def fun():
    print('inside fun')
    return gun

def gun(func_name):
    print('inside gun')
    func_name()

def main():
    gun(fun)

if __name__ =='__main__':
    main()