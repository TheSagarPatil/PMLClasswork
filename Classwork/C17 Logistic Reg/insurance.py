import pandas as pd
from matplotlib import pyplot as plt
from sklearn import model_selection
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split 

def logistics(path):
    df = pd.read_csv(path)
    print('-'*50)
    print(df.head())

    plt.scatter(df.age, df.bought_insurance, marker = '+', color = 'red')

    plt.show()

    X_train, X_test, y_train, y_test  = train_test_split(df[['age']], df.bought_insurance, train_size = 0.5)
    print('Independent variables')
    print(X_train)
    print('dependent variables')
    print(y_train)
    print('-'*50)

    model = LogisticRegression()
    model.fit(X_train, y_train )
    y_predicted = model.predict(X_test)
    print('predicted dependent val', y_predicted)
    print('Expected dependent var ', y_test)

    print('-' * 50 )

    data = model.predict_proba(X_test)
    print(' probability is ')
    print(data)

    print('confusion matrix')
    print(confusion_matrix(y_test, y_predicted))

    print('accuracy score ')
    print(accuracy_score(y_test, y_predicted))

def main():
    print('supervised Machine learning')
    logistics('H:\WORKSPACE\PML\PMLClasswork\Classwork\C17 Logistic Reg\data\insurance_data.csv')

if __name__ == '__main__':
    main()




