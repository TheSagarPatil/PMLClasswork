def outer():
    print('inside outer')
    def inner():
        print('inside inner')

    return inner

def main():
    func = outer()
    func()

if __name__ =='__main__':
    main()