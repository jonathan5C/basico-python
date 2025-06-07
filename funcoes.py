def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
         return 'Não será possível fazer a divisão, pois o valor inserido é 0'
    return a / b


valor_inicial = 7
valor_final = 0

resultado = divisao(valor_inicial, valor_final)
print(f'O resultado da operação foi {resultado}')