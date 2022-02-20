import pandas as PD
def main():
    data = PD.read_csv('H:\WORKSPACE\PML\PMLClasswork\Classwork\C17 Logistic Reg\data\data.csv')
    #print(data.shape)
    print(data.head())

if __name__ == '__main__':
    main()