from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import mglearn as MGL
import pandas as PD
from sklearn.neighbors import KNeighborsClassifier as KNN
import numpy as NP

def main():
    DSKeys={
        'allfeatures':'feature_names'
    }
    DATA = load_iris()

    print(f'Keys of iris {DATA.keys()}')

    print(DATA['DESCR'][:193])

    print(f'Target Names ',     DATA['target_names'] )

    print( 'feature Names',     DATA['feature_names'])

    print( 'Type of data',      type(DATA['data'])   )
    
    print( 'Type of target',    type(DATA['target']) )

    print( 'shape of target',   DATA['target'].shape )

    X_train, X_test, y_train, y_test = train_test_split(
        DATA['data'],
        DATA['target'],
        random_state= 0
    )

    print('X_train shape', X_train.shape)

    print('X test shape', X_test.shape)

    print('Y train shape', y_train.shape)

    print('Y test shape', y_test.shape)

    DATA_FRAME = PD.DataFrame(X_train, columns = DATA['feature_names'])

    PDPlot = PD.plotting
    PDPlot.scatter_matrix(
        DATA_FRAME, 
        c=y_train, 
        figsize=(15,5), 
        marker = 'o', 
        hist_kwds={'bins':20}, 
        s=60, 
        alpha=0.2
    )

    knn = KNN(n_neighbors=  1)
    knn.fit(X_train, y_train)

    res = knn.predict(X_test)
    print(f'Test predictions, {res}')

    print( f'Test score : { NP.mean( "y_pred" == y_test ) :.2f} ') 
    print(f'Test set score : { knn.score(X_test, y_test) :.2f}')


if __name__ == '__main__':
    main()