from sklearn.neural_network import MLPClassifier
from sklearn import datasets

iris = datasets.load_iris()

entradas = iris.data
saidas = iris.target

redeNeural = MLPClassifier(activation='logistic', verbose=True, max_iter=1000, 
                           tol=0.000001, learning_rate_init=0.3)
redeNeural.fit(entradas, saidas)