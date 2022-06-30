# Faça um Programa que converta metros para centímetros.

def medida():
    m = float(input('Digite o tamanho em metros: '))
    km = m * 0.001
    hm = m * 0.01
    dam = m * 0.1
    dm = m * 10
    cm = m * 100
    mm = m * 1000

    print('O número digitado foi: {}, resultado convertido: \n{} km \n{} hm \n{:.1f} dam \n{} dm \n{}cm \n{}mm'.format(m, km, hm, dam, dm, cm, mm))

medida()