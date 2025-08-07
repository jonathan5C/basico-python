# Escreva um programa para ler o ano de nascimento de uma pessoa e escrever uma
# mensagem que diga se ela poderá ou não votar este ano.

ano_atual = 2025

ano_nascimento = int(input('Informe o ano de nascimento: '))

diferenca = ano_atual - ano_nascimento

if diferenca < 18:
    print('Infelizmente, não tem idade para votar ainda!')
else:
    print('Você está apto para votar sim esse ano.')
