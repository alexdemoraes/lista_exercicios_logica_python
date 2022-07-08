# João Papo-de-Pescador, homem de bem, comprou um microcomputador
# para controlar o rendimento diário de seu trabalho. Toda vez que
# ele traz um peso de peixes maior que o estabelecido pelo regulamento
# de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de
# R$ 4,00 por quilo excedente.
# 
# João precisa que você faça um programa
# que leia a variável peso (peso de peixes) e calcule o excesso.

# Gravar na variável excesso a quantidade de quilos além do limite e
# na variável multa o valor da multa que João deverá pagar. 

# Imprima os dados do programa com as mensagens adequadas.


def peso_de_peixes():
    peso = int(input('Digite o peso: '))
    limite = 50
    multa_por_kg = 4
    excesso = 0

    if(peso > limite):
      excesso = peso - limite
      multa = excesso * multa_por_kg
      print('O peso limite é de: {} kgs. O valor do acréscimo fica em R$ {}, pelo excesso de: {} kgs'.format(limite, multa, excesso))

    else:
        print('Não ultrapassou o limite, então não será multado')
        
peso_de_peixes()


