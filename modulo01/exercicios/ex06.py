# Escreva um programa que calcule o perímetro e a área de um retângulo.

base = float(input('Informe a base do retângulo: '))
altura = float(input('Informe a altura do retângulo: '))

perimetro = 2 * (base + altura)
area = base * altura

print(f'O perímetro do retângulo é {perimetro}')
print(f'A área do retângulo é {area}')
