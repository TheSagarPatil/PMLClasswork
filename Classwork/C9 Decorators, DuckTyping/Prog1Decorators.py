import traceback
class Decos(object):
    @staticmethod
    def smartSub(func):
        def wrapper(no1, no2):
            if(no1 < no2):
                no1, no2 = no2, no1
            for line in traceback.format_stack():
                print(line.strip())
            return no1-no2
        return wrapper

SMART_SUB = Decos.smartSub

class Arithmatic(object):
    def __init__(self, no1, no2):
        self.iNo1 = no1
        self.iNo2 = no2

    @staticmethod
    @SMART_SUB
    def sub(no1, no2):
        return no1-no2

    def subtract(self):
        return Arithmatic.sub(self.iNo1, self.iNo2)

def main():
    a = Arithmatic(2,7)
    print(a.subtract())

if __name__ == '__main__':
    main()