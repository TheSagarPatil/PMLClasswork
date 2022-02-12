from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier 
from matplotlib import pyplot as PLT
import pandas as PD

def printFeaturesTargets ( DS_IRIS ):
    print('FEATURES \n',  DS_IRIS.feature_names)
    print('TARGET \n' ,   DS_IRIS.target_names)
def printDataSet(DS_IRIS):
    for i in range( len(DS_IRIS.data) ):
        print(f'{i :<5} | {DS_IRIS.data[i] } | {DS_IRIS.target[i] :<3}')

def main()-> None:
    DS_IRIS = load_iris()
    #print(DS_IRIS)
    #View dataset
    #print('First 10 elements from iris dataset')
    #printDataSet(DS_IRIS)
    #check features and targets
    printFeaturesTargets(DS_IRIS)

    DF = PD.DataFrame(  data = DS_IRIS.data, 
                        columns = DS_IRIS.feature_names
                    )

    KNN = KNeighborsClassifier()
    DTC = DecisionTreeClassifier()
    #print(DS_IRIS.data)
    trainFt, testFt, trainLb, testLb = train_test_split(X= DS_IRIS.data.feature_names, y= DS_IRIS['target'], test_size=0.50, train_size=50, shuffle=True)
    #DTC.fit()

if __name__ == '__main__':
    main()