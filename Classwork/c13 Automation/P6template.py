import sys as SYS
import time as T
import datetime as DT
import schedule as SCH

def mytask():
    print(f'task has run {DT.datetime.now()}')

def main():
    print('Periodic App')
    SCH.every(1).minutes.do(mytask)
    while True:
        SCH.run_pending()
        T.sleep(1)

if __name__ == '__main__':
    main()