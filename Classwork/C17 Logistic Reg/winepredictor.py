from sklearn import metrics as MTX
from sklearn import datasets as DS
from sklearn.neighbors import KNeighborsClassifier as _KNN
from sklearn.model_selection import train_test_split
import json as JSON
import pandas as PD

def printSeperator() -> None :
    print( '\n', '*-' * 50 , '\n' )

def load_data_set():
    return DS.load_wine()

def analyseData(data) -> None :
    #print the names of features
    print('Features \n\n', data.feature_names)
    printSeperator()

    #print the names of target 
    print('Targets \n\n', data.target_names)
    printSeperator()
    
def getDataFrame(data):
    
    _data = PD.DataFrame(data.data, )
    columns:list = list()
    columns.extend(data.feature_names)
    #print(columns)
    _data.columns = columns
    DF = _data
    
    print( DF.head() )
    printSeperator()

    print('Target \n\n')
    print(DF.target)
    printSeperator()

    return DF
    
def cleanData(df):
    return df 


def winePredictor ():
    #load toy dataset
    DATA = load_data_set()
    #run analysis code
    analyseData(DATA)
    #cleanseData
    #DF = getDataFrame(DATA)
    #DF = cleanData(DF)

    X_train, X_test, Y_train, Y_test = train_test_split(DATA.data, DATA.target, test_size=0.3)

    KNN = _KNN( n_neighbors = 3 )
    KNN.fit( X_train, Y_train )

    Y_pred = KNN.predict( X_test, )

    print('Accuracy' , MTX.accuracy_score(Y_test, Y_pred) )



def main():
    winePredictor()
    return 0

if __name__ == '__main__':
    main()