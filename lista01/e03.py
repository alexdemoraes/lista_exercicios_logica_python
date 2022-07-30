# Faça um Programa que peça dois números e imprima a soma

def soma(n1, n2):
    return n1 + n2

def main():
    n1 = int(input("Digite o primeiro número:"))
    n2 = int(input('Digite o segundo número: '))
    soma1 = soma(n1, n2)
    print('A soma dos números {} e {} é: {}'.format(n1, n2, soma1))


if __name__ == "__main__":
    main()
