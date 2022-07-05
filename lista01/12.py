# Tendo como dados de entrada a altura de uma pessoa,
# construa um algoritmo que calcule seu peso ideal,
# usando a seguinte fórmula: (72.7*altura) - 58

def peso_ideal():
    a = float(input('Digite a sua altura (ex: 1.70): '))
    p = (72.7 * a) - 58 
    
    return('O seu peso ideal é: {}'.format(p))

print (peso_ideal())