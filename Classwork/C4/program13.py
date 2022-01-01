END_OF_MESSAGE = '-----------\n'
def main():
    string = input("Enter a string \n" + END_OF_MESSAGE)
    for i in range(0, -5, -1):
        print(i, string)


if __name__ == '__main__':
    main()