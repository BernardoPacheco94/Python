meses = [
    {'mes': 'Janeiro', 'temperatura':35.8},
    {'mes': 'Fevereiro', 'temperatura':37},
    {'mes': 'Março', 'temperatura':34},
    {'mes': 'Abril', 'temperatura':12.6},
    {'mes': 'Maio', 'temperatura':11.9},
    {'mes': 'Junho', 'temperatura':10.5},
    {'mes': 'Julho', 'temperatura':15.5},
    {'mes': 'Agosto', 'temperatura':17.5},
    {'mes': 'Setembro', 'temperatura':18},
    {'mes': 'Outubro', 'temperatura':19.6},
    {'mes': 'Novembro', 'temperatura':22.1},
    {'mes': 'Dezembro', 'temperatura':32.6}
    ]

sensacao = ''
soma = 0
for mes in meses:
    if mes.get('temperatura') < 15:
        sensacao = 'Frio'
    else:
        sensacao = 'Quente'
    soma += mes.get('temperatura')
    print(mes.get('mes'),mes.get('temperatura'),'*C - Sensacao:',sensacao)
print('Média do ano:',round((soma/12),2),'*C')
