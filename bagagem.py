print('VERIFICAÇÃO DE BAGAGEM')
bagagem = float(input('Quantos Kg a bagagem possui?'))
excedente = bagagem-10

if bagagem > 10:
    print('\nLimite de peso excedido em:',excedente,'Kg\nValor adicional R$:',round( (excedente*2), 3) )
else:
    print('Bagagem dentro do limite')
print('\nBOA VIAGEM!')