print('ORÇAMENTO:')

cliente = input('informe o nome do cliente: ')
modelo = input('Qual o modelo do aparelho?')
vl_compra = float(input('Qual o valor de compra do aparelho?'))

print(40*'-')
print('ORÇAMENTO DO', modelo.upper())
print('Cliente: ',cliente)
print('Valor Total: R$ ',vl_compra+400)
print(40*'-')