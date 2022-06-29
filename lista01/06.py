# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

from cmath import pi

def area():
    r = float(input('\nDigite o raio do seu círculo: '))
    a = pi * r**2
    return print('A sua área é: {:.2f}'.format(a))

area()
    