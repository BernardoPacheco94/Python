print('CARRINHO DE COMPRAS')
vl_total = float(input('Informe o valor do produto:'))
cupom = input('Possui cupom de desconto?').upper().replace(' ','')

if cupom == 'CUPOM10':
    vl_total = vl_total-(vl_total*0.1)
    
elif cupom == 'CUPOM25':
    vl_total = vl_total-(vl_total*0.25)
print('Valor total: R$',round(vl_total,3))
    