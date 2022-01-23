#import sys as SYS
from sys import *
import os as OS
import json as JSON
def main():
    #ARG = SYS.argv
    ARG = argv
    #firstNo = int(ARG[1])
    #secondNo = int(ARG[2])
    #print(f'{int(firstNo)} , {int(secondNo)}')
    #adtn = firstNo + secondNo
    #print(f'Addidtion is {adtn}')
    if ( '--h' in ARG):
        print('--h')

if(__name__ == '__main__'):
    main()