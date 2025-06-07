lista = [1, 3, 5, 9, 8, 3, 3, 3]

lista.append(7)
lista.sort()
total_numero = lista.count(3)

print(len(lista))

if 9 not in lista:
    print('Contem o número 9')