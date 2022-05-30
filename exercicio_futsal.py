print('TIMES FUTSAL')

time_a = []
time_b = []

for i in range(1,11):
    nome = input('Nome:')
    nr_camisa = int(input('Camisa:'))
        
    if len(time_a) < 5:
        time_a.append({'nome': nome, 'nr_camisa': nr_camisa})
    else:
        time_b.append({'nome': nome, 'nr_camisa': nr_camisa})

print('ESCALAÇÃO TIME A:')
for jogador in time_a:
    print(jogador.get('nr_camisa'),jogador.get('nome'))
    

print('ESCALAÇÃO TIME B:')
for jogador in time_b:
    print(jogador.get('nr_camisa'),jogador.get('nome'))