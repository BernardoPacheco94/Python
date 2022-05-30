print('VERIFICAÇÃO DE IDADE')
nome = input('Informe seu nome:')
idade = int(input('Informe a sua idade:'))

if idade > 20:
    print(nome.title(),'é maior de idade')
else:
    print(nome.title(), 'é menor de idade')