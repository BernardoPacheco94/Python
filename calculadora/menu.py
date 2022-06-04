def mostrar_menu ():
    print('*****************CALCULADORA*****************')
    print('Escolha a opção desejada:')
    print('1 - SOMA              3 - MULTIPLICAÇÃO')
    print('2 - SUBTRAÇÃO         4 - DIVISÃO')
    print('              5 - SAIR')
    return int(input('Opção:'))

def capturar_numeros():
    nr_1 = float(input('Informe o primeiro número:'))
    nr_2 = float(input('Informe o segundo número:'))
    return nr_1, nr_2