peso = float(input('Informe seu peso em KG'))
altura = float(input('Informe sua altura em Metro'))

imc = peso/(altura*altura)
classificacao = None

if imc < 18.5:
    classificacao = 'Abaixo do Peso'
elif imc < 24.9:
    classificacao = 'Peso Normal'
elif imc < 29.9:
    classificacao = 'Sobrepeso'
elif imc < 34.9:
    classificacao = 'Obesidade Grau I'
else:
    classificacao = 'Obesidade Grau II'

print(f'Com peso {peso} e altura {altura} seu imc é {round(imc,2)}:')
print('Classificação:',classificacao)