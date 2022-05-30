jogadores = []

jogador_1 = {'nome': 'bernardo', 'pontuacao':0}
jogador_2 = {'nome': 'marcelo', 'pontuacao':0}

jogadores.append(jogador_1)#adicionando jogador na lista jogadores
jogadores.append(jogador_2)


print(jogadores)#toda lista
print(jogadores[0])#primeiro indice da lista é um dict
print(jogadores[0].get('nome'))#pegando um elemendo do dict pelo indice

for jogador in jogadores:#esse for retorna um dict
    print ('Jogador:',jogador.get('nome').title(), '| Pontuação:',jogador.get('pontuacao'))

print('')
jogadores[0]['pontuacao'] = 10#insere o valor no dict [0] no item 'pontuacao'
for jogador in jogadores:
    print ('Jogador:',jogador.get('nome').title(), '| Pontuação:',jogador.get('pontuacao'))