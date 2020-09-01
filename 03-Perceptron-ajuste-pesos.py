
import numpy as np

entradas  = np.array([[0,0], [0, 1], [1, 0], [1, 1]])
saidas = np.array([0,0,0,1])

pesos = np.array([0.0, 0.0])
taxaAprendizagem = 0.1

#Função de Ativação da rede | StepFunction
def stepFunction(soma):
    if (soma >= 1):
        return 1
    return 0

def calculaSaida(registro):
    saida = registro.dot(pesos)
    return(stepFunction(saida))


def treinar():
    erroTotal = 1
    while erroTotal != 0:
        erroTotal = 0
        for i in range(len(saidas)):
            print(saidas[i])
            saidaCalculada = calculaSaida(np.asarray(entradas[i]))
            erro = saidas[i] - saidaCalculada
            erroTotal += erro
            for j in range(len(pesos)):
                pesos[j] = pesos[j] + (taxaAprendizagem * entradas[i][j] * erro)
                print(f'Pesos Atualizados: {pesos[j]}')

    print(f'total Erros: {erroTotal}')

treinar