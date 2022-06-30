# Faça um Programa que peça a temperatura em graus 
# Celsius, transforme e mostre em graus Fahrenheit.

def temperatura():
    c = float(input('\nDigite o valor em graus Celsius a ser convertido: '))
    f = c * (9 / 5) + 32
    
    return print('O valor convertido em Fahrenheit é: {}°F'.format(f))

temperatura()