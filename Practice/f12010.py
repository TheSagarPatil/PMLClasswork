import pandas as PD
import numpy as NP

POINTS_2010 = {
    '1':25,
    '2':18,
    '3':15,
    '4':12,
    '5':10,
    '6':8,
    '7':6,
    '8':4,
    '9':2,
    '10':1,
    None:'ERROR',
    'nan':0
}
POINTS=POINTS_2010

def getData():
    return PD.read_csv('./datasets/F12010_Standings.csv')
def main():
    DF = getData()
    #print(DF)

    DF = DF.drop('Pos.', axis='columns')
    #DF = DF.T
    tableDetail = {}
    #print(DF)
    """for index, row in DF.iterrows():
        driverName = row['Driver']
        tableDetail[driverName] = {}
        for index, dataItem in row.iteritems():
            item = tableDetail[driverName]
            if(index != 'Driver' and 'Points'):
                item[index] = dataItem

    for driver in tableDetail:
        TABLE = tableDetail
        for round in TABLE[driver]:
            if(round != 'Points'):
                print(driver , ':' , round , ':' , TABLE[driver][round])"""


    print(type(f1))
    print(tableDetail)


def f1():
    pass
    
if(__name__ == '__main__'):
    main()