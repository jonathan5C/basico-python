"""
    Tipos Primitivos na linguagem
    int (Inteiro)
    float (Float)
    str (String)
    bool (Boolean)

    Observação: Lembrando que a linguagem não é fortemente tipada, por isso a declaração de variáveis é diferente.
    Também não é necessário colocar ";" no final das linhas, fica opcional.
"""

# Trabalhando com inteiros
anoHoje = 2025
anoNascimento = 2002

resultado = anoHoje - anoNascimento
print(resultado)


# Trabalhando com float
horasFinal = 2.9
horasInicial = 0.5

resultadoHoras = horasFinal * horasInicial
print('Multiplicação de horas')
print(resultadoHoras)


# Trabalhando com String
nome = 'Jonathan'

# print('Seu nome é:', nome)
print(f'Seu nome é {nome}')

# Trabalhando com Boolean
eVerdadeiro = False

print('Esse ano é 2023?', eVerdadeiro)

# Receber dados do usuário no terminal

# Exemplo de entrada com string
nome_completo = input('Informe o seu nome completo: ')

# Exemplo de entrada com números
idade_usuario = int(input('Informe a sua idade: '))
print(f'O usuário {nome_completo} tem {idade_usuario} anos.')

"""
    Controle de Fluxo
    if
    else
    elif

    Esses são as palavras reservadas para definir um controle de fluxo, que é uma decisão
    que o desenvolver precisa tomar com blocos de verdadeiro ou falso. Dentro há operadores
    lógicos: and, or e not.
"""

# Exemplo simples
temperatura = 30
if temperatura > 25:
    print("Dia quente!")
elif temperatura > 15:
    print("Dia agradável!")
else:
    print("Dia frio!")

# Exemplo mais complexo
idade = 20
tem_assinatura_premium = True

if idade > 18 and tem_assinatura_premium:
    print("Acesso ilimitado a todo o conteúdo premium.")
elif idade > 18:
    print("Acesso limitado. Considere assinar o plano premium para mais benefícios.")
else:
    print("Acesso restrito a conteúdo adequado para menores de 18 anos.")
