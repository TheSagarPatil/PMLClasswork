from sklearn.linear_model import LinearRegression as LR
import numpy as np

x = np.array([5,15,25,35,45,55]).reshape((-1,1))
y = np.array([5,20,14,32,22,38])

x2 = [[5, 15, 21],[15, 56, 12],[25, 45, 21]]
y2 = [5,20,14]


model = LR()

model.fit(x,y)

rsq = model.score(x,y)
print(f'coeffiecient of determination is RSqare Value  is {rsq}')
print(f'intercept', model.intercept_)
print(f'slope {model.coef_}')
ypred = model.predict(x)
print(f'predicted response {ypred}',sep='\n')
ypred = model.intercept_ + ( model.coef_ * x )
print(f'predicted response {ypred}')