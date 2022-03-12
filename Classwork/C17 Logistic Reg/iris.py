import pandas as PD
import numpy as NP
import matplotlib.pyplot as PLT
from sklearn.model_selection import train_test_split as TTS
from sklearn.neighbors import KNeighborsClassifier as KNC
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier
def getData():
    #return PD.read_csv('H:\WORKSPACE\PML\PMLClasswork\Classwork\C17 Logistic Reg\data\kmeans.csv')
    return PD.read_csv('H:\WORKSPACE\PML\PMLClasswork\Classwork\C17 Logistic Reg\data\iris.csv')
    #26,16 68,42 55,76
def diab():
    DATASET = getData()

    x = DATASET.iloc[:, [0, 1, 2, 3]].values

    #finding optimum number of cluster for k means classifications
    wcss = []

    for i in range(1,11):
        kmeans = KMeans (
            n_clusters = i ,
            init = 'k-means++',
            max_iter = 300 ,
            n_init = 100 ,
            random_state= 0
        )
        kmeans.fit(x)
        wcss.append(kmeans.inertia_)

    #plotting the result onto a line graph allowing us to observe 'the elbow'
    PLT.plot(range(1,11), wcss)
    PLT.title('Elbow Method')
    PLT.xlabel('Number of clusters')
    PLT.ylabel('WCSS') #within cluster sum of squares
    PLT.show()

    #applying kmeans to the dataset / creating the kmeans classifier
    kmeans = KMeans(n_clusters = 3,
        init = 'k-means++',
        max_iter = 300,
        n_init = 10,
        random_state = 0
    )
    y_kmeans = kmeans.fit_predict(x)

    #Visualize graps

    PLT.scatter(
        x[y_kmeans == 0, 0],
        x[y_kmeans == 0, 1],
        s = 100,
        c = 'red',
        label = 'iris-setosa'
    )
    PLT.scatter(
        x[y_kmeans == 1, 0],
        x[y_kmeans == 1, 1],
        s = 100,
        c = 'blue',
        label = 'iris-versicolor'
    )
    PLT.scatter(
        x[y_kmeans == 2, 0],
        x[y_kmeans == 2, 1],
        s = 100,
        c = 'green',
        label = 'iris-virginica'
    )

    #Plotting the centroids of the clusters

    PLT.scatter(
        kmeans.cluster_centers_[:, 0],
        kmeans.cluster_centers_[:, 1],
        s = 100,
        c = 'yellow',
        label = 'Centroids'
    )
    PLT.legend()
    PLT.show()

def main():
    print('Diabetis classifier')
    diab()
main()