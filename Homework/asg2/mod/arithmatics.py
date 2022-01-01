def add(*argv):
    sum=0
    for n in argv:
        sum+=n
    return sum

def sub(n1, n2):
    return n1-n2

def mult(*argv):
    sum = 1
    for n in argv:
        sum *=n
    return sum

def div(n1, n2):
    return n1 // n2
