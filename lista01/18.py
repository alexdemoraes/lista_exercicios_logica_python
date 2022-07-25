# Faça um programa que peça o tamanho de um arquivo
# para download (em MB) e a velocidade de um link de
# Internet (em Mbps), calcule e informe o tempo aproximado
# de download do arquivo usando este link (em minutos)


print('\n')

def tamanho_arquivo():
    mb = int(input('Digite o tamanho do arquivo em MB para fazer download: '))
    velocidade = int(input('Digite a velocidade do link em Mbps: '))

    print('\n')

    tempo = (mb / (velocidade / 8)) / 60

    # tempo = mb / velocidade
    # final = tempo / 60

    return ('O tempo aproximado de download é de {:.0f} minutos.'.format(tempo))

print(tamanho_arquivo())

# Formula para calcular o tempo de download
# Tamanho do arquivo em megabytes / (velocidade de download em megabits / 8) = tempo em segundos.
# Para minutos dividir por 60 ( / 60)