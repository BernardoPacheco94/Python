try:
    num = int(input('Digite um valor entre 10 e 20'))
    if num < 10 or num > 20:
        raise Exception(f'{num} não está entre 10 e 20')
    print(f'O dobro de {num} é {num * 2}')
except Exception as e:
    print(e)