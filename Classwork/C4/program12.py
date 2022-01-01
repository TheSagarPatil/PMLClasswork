import math as M
def myGenerator(start, stop, step):
    for i in range(start, stop, step):
        yield i

def getNumberFromConsole(message=""):
    ret = input(message+'\n')
    try :
        return int(ret)
    except ValueError:
        return getNumberFromConsole("Please correct Input \n" + message)

def main():
    stop  = getNumberFromConsole("How many iterations?")
    start = 0
    step  = 1

    for i in myGenerator(0, stop, 1):
        print(i)

if(__name__ == '__main__'):
    main()