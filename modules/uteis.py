def fatorial(num):
    numero_fatorial = 1

    for count in range(1, num + 1):
        numero_fatorial *= count
    
    return numero_fatorial
