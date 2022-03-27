from matplotlib import pyplot
import pandas as PD
import seaborn as SNS
from sklearn.svm import SVC as SVC
import matplotlib.pyplot as PLT
from sklearn.metrics import confusion_matrix as ConfMx
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score

def svmiris(url) -> None:
    colnames = [
        'sepal_length',
        'sepal_width',
        'petal_length',
        'petal_width',
        'class'
    ]

    DATASET = getDataset(url, colnames)
    DATASET = encodeDataset(DATASET)

    x = DATASET.iloc[:,:-1]
    y = DATASET.iloc[:, -1].values

    #print(y)

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state = 0)
    classifier = SVC(kernel = 'linear', random_state = 0)
    classifier.fit(x_train, y_train)
    y_pred = classifier.predict(x_test)

    cm = ConfMx(y_test, y_pred)
    print(cm)

    accuracies = cross_val_score(
        estimator=classifier,
        X = x_train,
        y = y_train,
        cv = 10
    )
    print(f'Accuracy {accuracies.mean() * 100 :.2f}')
# END MAIN

def encodeDataset(DS : PD.DataFrame ) -> PD.DataFrame:
    """@help
@param : DS (pandas dataframe)
@return : DS (pandas dataframe)
@var Encoder (Dictionary) : Encodes categorical data using encoder.
    """
    encoderDict : dict = {
        'class' : {
            'Iris-setosa':      1,
            'Iris-versicolor':  2,
            'Iris-virginica':   3,
        }
    }
    DS = DS.replace( encoderDict )
    print( 'After Encoding data set is' )
    print( DS.head() )
    return DS

def main():
    #showDocumentation()
    svmiris("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")

def showDocumentation():
    funcs = [
        encodeDataset,
    ]
    for func in funcs:
        help(func)

def getDataset(url, columnNames):
    data = PD.read_csv(url, names = columnNames)
    print('dataset loaded successfully')
    print(data.head())
    return data

if __name__ == '__main__':
    main()