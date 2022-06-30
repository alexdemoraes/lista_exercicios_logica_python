# Faça um Programa que peça a temperatura em graus Fahrenheit,
# transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

def temperatura():
    f = float(input('\nDigite a temperatura em Fahrenheit: '))
    c = 5 *((f - 32) / 9)

    return print('A temperatura convertida em graus Celsius é: {}°C'.format(c))

temperatura()