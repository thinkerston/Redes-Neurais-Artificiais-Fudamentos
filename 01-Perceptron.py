entradas = [-1, 7, 5]
pesos = [0.8, 0.1, 0]

#Função de entrada e peso
def soma(entradas, pesos):
    s = 0
    for valor in range(3):
        # print(entradas[valor])
        # print(pesos[valor])
        s += entradas[valor] * pesos[valor]
    
    return s


valor = soma(entradas, pesos)
print(f'soma: {valor}')


#Função de Ativação da rede | StepFunction
def stepFunction(soma):
    if (soma >= 1):
        return 1
    return 0


result = stepFunction(valor)
print(f'Função de Ativação: {result}')
