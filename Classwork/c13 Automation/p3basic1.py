#import sys as SYS
from sys import *
import os as OS
import json as JSON
def main():
    #ARG = SYS.argv
    ARG = argv
    print(f'File Name : {ARG[0]}')
    print(enumerate(ARG))
    for i, arg in enumerate(ARG):
        print(f'{i}. {arg}')

if(__name__ == '__main__'):
    main()