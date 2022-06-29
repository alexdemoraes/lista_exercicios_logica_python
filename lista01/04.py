# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

def notas():
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    n3 = float(input('Digite a terceira nota: '))
    n4 = float(input('Digite a quarta nota: '))

    media = (n1 + n2 + n3 + n4) / 4
    
    print('\nO resultado da sua média é: {:.1f}'.format(media))
notas()


