import numpy as np
from sklearn import datasets


def sigmoid(soma):
	return 1 / (1 + np.exp(-soma))


def derivadaSigmoid(sig):
	return sig *(1 - sig)


entradas = np.array([[0,0],
					 [0,1],
					 [1,0],
					 [1,1]])

saidas = np.array([[0], [1], [1], [0]])

base = datasets.load_breast_cancer()

entradas = base.data
valoresSaidas = base.target
saidas = np.empty([569, 1], dtype=int)
for i in range(569):
	saidas[i] = valoresSaidas[i]


pesos_0 = 2 * np.random.random((30,5)) -1
pesos_1 = 2 * np.random.random((5, 1)) -1

epocas = 100000

momento = 1
taxaDeAprendizagem = 0.3

for j in range(epocas):
	camadasEntrada = entradas
	somaSinapse_0 = np.dot(camadasEntrada, pesos_0)
	camadaOculta = sigmoid(somaSinapse_0)

	somaSinapse_1= np.dot(camadaOculta, pesos_1)
	camada_saida = sigmoid(somaSinapse_1)

	erroCamadaSaida = saidas - camada_saida
	mediaAbsoluta = np.mean(np.abs(erroCamadaSaida))
	print(f'EPOCH: {j}, Erro: {mediaAbsoluta}')


	derivada_saida = derivadaSigmoid(camada_saida)
	delta_saida = erroCamadaSaida * derivada_saida

	pesos_transpostos = pesos_1.T
	deltaSaidaXPeso = delta_saida.dot(pesos_transpostos)
	deltaCamadaOculta = deltaSaidaXPeso * derivadaSigmoid(camadaOculta)

	camadaOcultaTransposta = camadaOculta.T
	pesos_novo_1 = camadaOcultaTransposta.dot(delta_saida)
	pesos_1 = (pesos_1 * momento) + (pesos_novo_1 * taxaDeAprendizagem)

	camadasEntradaTransposta = camadasEntrada.T
	pesos_novos_0 = camadasEntradaTransposta.dot(deltaCamadaOculta)
	pesos_0 = (pesos_0 * momento) + (pesos_novos_0 * taxaDeAprendizagem)

