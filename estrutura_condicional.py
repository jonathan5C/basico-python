# Operadores lógicos
'''
Na linguagem temos três operadores lógicos:
    - and (e) - todas as afirmações precisam ser verdadeiras para passar
    - or (ou) - uma das condições precisa ser verdadeiras
    - not (negação) - vai negar a condição
'''

nome = str(input("Qual é o seu nome? "))
idade = int(input('Qual é a sua idade? '))

# if idade > 15:
#     print(f"A pessoa, chamada(o) {nome}, tem mais de 15 anos")
# else:
#     print(f"A pessoa, chamada(o) {nome}, só tem {idade} anos")


if idade > 18 and nome == 'Jonathan':
    print(f'O {nome} tem mais de 18 anos')
elif idade < 18 and idade >= 12:
    print(f'A pessoa tem entre 12 a 18 anos')
else:
    print(f'{nome} é uma criança ainda!')