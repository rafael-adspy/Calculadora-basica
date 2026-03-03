from time import sleep

def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a /  b


def menu_opçoes():
    print('''\n=====CALCULADORA.PY=====
    [1] SOMAR
    [2] SUBTRAIR
    [3] MULTIPLICAR
    [4] DIVIDIR
    [5] SAIR ''')


def pedir_numeros():
    while True:
        try:
            n1 = int(input('Digite o primeiro número: '))
            n2 = int(input('Digite o segundo número: '))
            return n1, n2
        except ValueError:
            print('Digite Apenas Números Inteiros')


def calculando():
    print('CALCULANDO...')
    sleep(2)


while True:
    menu_opçoes()
    op = input('Digite uma opção: ')

    if op == '5':
        print('Saindo...')
        sleep(2)
        break

    if op == '1':
        operação = somar
        sinal = '+'

    elif op == '2':
        operação = subtrair
        sinal = '-'

    elif op == '3':
        operação = multiplicar
        sinal = '*'
    elif op == '4':
        operação = dividir
        sinal = '/'

    else:
        print('Operação invalida!')
        continue

    n1, n2 = pedir_numeros()

    try:
        resultado = operação(n1, n2)
        print(f'{n1} {sinal} {n2} = {resultado}')

    except ZeroDivisionError:
        print('Erro numero dividido por zero!')



