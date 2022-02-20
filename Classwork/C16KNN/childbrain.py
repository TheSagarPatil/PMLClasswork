#linear regression algo

import numpy as NP
import pandas as PD
import matplotlib.pyplot as PLT

def getDataSetPath():
    return 'H:\WORKSPACE\PML\PMLClasswork\Classwork\C16KNN\headbrain.csv'
def main():
    data = PD.read_csv(getDataSetPath())
    X = data['Head Size(cm^3)'].values
    Y = data['Brain Weight(grams)'].values

    mean_x = NP.mean(X) #x bar
    mean_y = NP.mean(Y) #y bar

    n = len(X) #number of observations

    numerator = 0
    denomenator = 0

    #Line : y = mx + c
    # 

    for i in range(n):
        #Sum of (X-XBar) * (Y - YBar)
        numerator+= ( X[i] - mean_x ) * (Y[i] - mean_y) 
        #Sum of (X-XBar) ** 2
        denomenator += (X[i] - mean_x) ** 2

    m = numerator / denomenator

    #Y intercept of reg line : c = YBar - ( m * XBar )
    c = mean_y - (m * mean_x)

    print("Slope of regression line is ", m)
    print("Y intercept of regression line is", c)

    max_x = NP.max(X) + 100
    min_x = NP.min(X) + 100

    #displaying plot of above points

    x = NP.linspace(min_x, max_x, n)

    y = ( m * x ) + c

    PLT.plot(x,y, color = '#58b970', label = 'Regression Line')
    PLT.scatter(X,Y, color='#ef5423', label = 'Scatter Plot')

    PLT.xlabel('Head Size')
    PLT.ylabel('Brain Weight')
    PLT.legend()
    PLT.show()

    ss_t = 0
    ss_r = 0

    for i in range(n):
        y_pred = c + (m * X[i])
        ss_t += ( Y[i] - mean_y ) ** 2
        ss_r += ( Y[i] - y_pred ) ** 2

    rSq = 1 - ( ss_r / ss_t )
    print(f'RSquare is {rSq}')

    #print(data)

if __name__ == '__main__':
    main()