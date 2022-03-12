import pandas as PD
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn import datasets as DS 

from sklearn.ensemble import VotingClassifier

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

def SagarVotingClassifier():

    #iris = load_iris()
    iris = DS.load_iris()

    x = iris['data']
    y = iris['target']

    log_clf = LogisticRegression()
    rnd_clf = RandomForestClassifier()
    knn_clf = KNeighborsClassifier()

    x_train, x_test, y_train, y_test = train_test_split(x,y,random_state=42, train_size=0.85)
    vot_clf = VotingClassifier(estimators = [
            ('ir', log_clf),
            ('rnd', rnd_clf),
            ('knn', knn_clf)
        ],
        voting='hard' #soft
    )

    vot_clf.fit(x_train, y_train)
    pred = vot_clf.predict(x_test)

    print('testing accuracy', accuracy_score(y_test, pred) * 100)

def main():
    SagarVotingClassifier()

if __name__ == '__main__':
    main()

