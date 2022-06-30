# Faça um Programa que calcule a área de um quadrado, 
# em seguida mostre o dobro desta área para o usuário.

def quadrado():
    q = float(input('Digite a área do quadrado: '))
    a = q * q
    d = a * 2
    return print('O resultado do dobro da área é: {}'.format(d))

quadrado()