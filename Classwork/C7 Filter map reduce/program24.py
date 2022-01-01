from functools import reduce
lm_add2 = lambda x,y:x+y 
lm_add  = lambda *x : reduce(lm_add2, x)
#lm_add  = lambda *x : (print(i) for i in x)
def Add(a,b):
    return a+b
def main():
    print(Add(10,20))
    print(lm_add(10,20,30))

if(__name__ == '__main__'):
    main()