import numpy as np

def sigmoid(soma):
	return 1 / (1 + np.exp(-soma))

entradas = np.array([[0,0],
					 [0,1],
					 [1,0],
					 [1,1]])

saidas = np.array([[0], [1], [1], [0]])

pesos_0 = np.array([[-.424, -.740, -.961],
					[.358, -.577, -.469]])

pesos_1 = np.array([[-.017], [-.893], [.148]])

epocas = 100

for j in range(epocas):
	camadasEntrada = entradas
	somaSinapse_0 = np.dot(camadasEntrada, pesos_0)
	camadaOculta = sigmoid(somaSinapse_0)

	somaSinapse_1= np.dot(camadaOculta, pesos_1)
	camada_saida = sigmoid(somaSinapse_1)