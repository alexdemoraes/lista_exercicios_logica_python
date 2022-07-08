# Faça um Programa para uma loja de tintas. O programa
# deverá pedir o tamanho em metros quadrados da área a
# ser pintada. Considere que a cobertura da tinta é de
# 1 litro para cada 6 metros quadrados e que a tinta é
# vendida em latas de 18 litros, que custam R$ 80,00 ou
# em galões de 3,6 litros, que custam R$ 25,00.

# Informe ao usuário as quantidades de tinta a serem
# compradas e os respectivos preços em 3 situações:

# comprar apenas latas de 18 litros;

# comprar apenas galões de 3,6 litros;

# misturar latas e galões, de forma que o desperdício de
# tinta seja menor. Acrescente 10% de folga e sempre
# arredonde os valores para cima, isto é, considere latas cheias.



import math

print('\n')

def  apenas_latas():

    metros = int(input('Digite quantos m² você deseja pintar? '))
    
    litros_latas = 18
    valor_lata = 80
    
    litros = (metros / 6) * 1.1    # seria os 10% de acréscimo
    num_latas = math.ceil(litros / litros_latas)
    valor_total = num_latas * valor_lata

    return('Você deverá usar {} latas de 18 litros e o valor ficará em R$ {:.2f}'.format(num_latas, valor_total))

print(apenas_latas())


print('\n')


def apenas_galoes():

    metros = int(input('Digite quantos m² você deseja pintar? '))
    
    litros_galao = 3.6
    valor_galao = 25

    litros = (metros / 6) * 1.1
    num_galoes = math.ceil(litros / litros_galao)
    valor_total = num_galoes * valor_galao

    return('Você deverá usar {} galões de 3.6 litros e o valor ficará em R$ {:.2f}'.format(num_galoes, valor_total))

print(apenas_galoes())


print('\n')


def mescla_entre_galoes_e_latas():

    metros = int(input('Digite quantos m² você deseja pintar? '))

    litros_latas = 18
    valor_lata = 80
    litros_galao = 3.6
    valor_galao = 25

    litros = (metros / 6) * 1.1

    num_latas = math.floor(litros / litros_latas)
    valor_latas = num_latas * valor_lata

    litros_faltantes = litros % litros_latas

    num_galoes = math.ceil(litros_faltantes / litros_galao)
    valor_galoes = num_galoes * valor_galao

    valor_total = valor_latas + valor_galoes

    return('Você deverá usar {} latas de 18 litros e mais {} galões de 3.6 litros, no valor de R$ {}'. format(num_latas, num_galoes, valor_total))
 
print(mescla_entre_galoes_e_latas())