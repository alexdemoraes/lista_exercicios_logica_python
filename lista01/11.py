# Faça um Programa que peça 2 números inteiros e um número real.
# Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

def numero():
    n1 = int(input('\nDigite um número inteiro: '))
    n2 = int(input('Digite outro número inteiro: '))
    n3 = float(input('Digite outro número, agora real: '))
    
    r1 = (n1 * 2) + (n2 / 2)
    print('\nResultado da primeira questão: {:.0f}'.format(r1))

    r2 = (n1 * 3) + n3
    print('Resultado da segunda questão: {}'.format(r2))

    r3 = n3**3
    print('Resultado da terceira questão: {}'.format(r3))

numero()