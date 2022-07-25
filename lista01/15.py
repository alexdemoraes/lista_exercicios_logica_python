# Faça um Programa que pergunte quanto você ganha por hora
# e o número de horas trabalhadas no mês. Calcule e mostre
# o total do seu salário no referido mês, sabendo-se que são
# descontados 11% para o Imposto de Renda, 8% para o INSS e
# 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.

# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$

# Obs.: Salário Bruto - Descontos = Salário Líquido.


print('\n')

def salario_mes():
    sal_hora = float(input('Quanto você ganha por hora? '))
    horas_trabalhadas = int(input('Quantas horas você trabalhou neste mês? '))

    print('\n')

    salario_bruto = sal_hora * horas_trabalhadas

    ir = salario_bruto * (11 / 100)
    inss = salario_bruto * (8 / 100)
    sindicato = salario_bruto * (5 / 100)

    # salario_liquido = salario_bruto - ir - inss - sindicato

    desconto = ir + inss + sindicato

    salario_liquido = salario_bruto - desconto

    return ('O seu salário bruto é: R$ {:.2f} \n'
    'valor de contribuição: \n'
    'INSS: R$ {:.2f} \n'
    'IR: R$ {:.2f} \n'
    'Sindicato: R$ {:.2f} \n'
    'Seu salário líquido é: R$ {:.2f} \n'. format(salario_bruto, inss, ir, sindicato, salario_liquido))

print(salario_mes())
