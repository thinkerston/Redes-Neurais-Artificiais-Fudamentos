import numpy as np

entradas = np.array([-1, 7, 5])
pesos = np.array([0.8, 0.1, 0])

#Função de entrada e peso
def soma(entradas, pesos):
    
    #retornando o produto escalar da entrada sobre o peso
    return(entradas.dot(pesos))

valor = soma(entradas, pesos)
print(f'soma: {valor}')


#Função de Ativação da rede | StepFunction
def stepFunction(soma):
    if (soma >= 1):
        return 1
    return 0


result = stepFunction(valor)
print(f'Função de Ativação: {result}')
