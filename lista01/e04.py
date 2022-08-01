# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

def notas(n1, n2, n3, n4):
    return (n1 + n2 + n3 + n4) / 4

def main():
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    n3 = float(input('Digite a terceira nota: '))
    n4 = float(input('Digite a quarta nota: '))
    media = notas(n1, n2, n3, n4)

    print('\nO resultado da sua média é: {:.1f}'.format(media))


if __name__ == "__main__":
    main()




