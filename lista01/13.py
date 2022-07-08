# Tendo como dado de entrada a altura (h) de uma pessoa,
# construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7


print('\n')

def homem():
    a = float(input('Digite a sua altura (ex: 1.70): '))
    r = (72.7 * a) - 58
    return('O peso ideal para um homem é: {:.2f}'.format(r))

print('\n')

def mulher():
    a = float(input("Digite a sua altura (ex: 1.50): "))
    r = (62.1 * a) - 44.7
    return('O peso ideal para uma mulher é: {:.2f}'.format(r))


sexo = input('Digite se você é homem ou mulher: ')
if (sexo == 'homem'):
    print (homem())

elif (sexo == 'mulher'):
    print(mulher())

else:
    print('Valor inválido')

    