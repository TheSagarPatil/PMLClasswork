def division(a,b):
    ans = 0.0
    try:
        ans = a/b
    except(Exception):
        print('Zero Division Error')
    finally:
        print('Finally block')
    #critical statement, a statement which may generate exception
    return ans

def main():
    no1 = 1
    no2 = 0
    res = division(no1, no2)
    print(res)

if __name__ == '__main__':
    main()
