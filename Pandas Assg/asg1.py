import pandas as PD
import numpy as NP

CSVDATA = PD.read_csv('./datasets/breast-cancer-wisconsin.csv')

#print(CSVDATA.describe())
#print(CSVDATA)

data = NP.array([1,2,3,4,5])
s = PD.Series(data, index=[0,1,2,3,4]) #Extra index doesnt add up
print(s)
print(s[-3:])
print(s[0:-3])
print(s[0::2]) #from 0 to end, each second element
#print(s[6]) #KeyError

DF_DATA = [['a1', 1, 2],['b2', 2, 2],['c3', 3, 2],['d4', 4, 2], ['e5', 2], ['f6']]
COLUMNS = ['StudentName', 'RollNumber', 'Marks']
df = PD.DataFrame(DF_DATA, columns=COLUMNS)

print(df)

df2 = PD.DataFrame([['G7', 8, None ], ['H8',8]], columns=COLUMNS)
df = df.append(df2)
df['combined'] = df['Marks'] + df['RollNumber']
print(df)

print(df.iloc[7])