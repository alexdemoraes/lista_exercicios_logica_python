# Faça um Programa que pergunte quanto você ganha
# por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

def salario():
    sal_hora = float(input('\nQuanto você ganha por hora? R$ '))
    h_tra = int(input('Quantas horas você trabalhou este mês? '))
    sal_mes = sal_hora * h_tra

    return print('\nO seu salário este mês é: R$ {:.2f}'.format(sal_mes))

salario()