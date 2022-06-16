nome_produto = input('Informe o nome do produto:')
preco = float(input('Valor do produto:'))
tx_imposto = float(input('Informe a alíquota de imposto'))

vl_imposto = (tx_imposto/100)*preco

print('Resultado:')
print('Produto', nome_produto)
print('Preço de custo R$:', round(preco,2))
print('Valor de imposto R$:', round(vl_imposto,2))
print(f'\nVALOR FINAL DO {nome_produto.upper()} R$:{round(preco+vl_imposto,2)}')