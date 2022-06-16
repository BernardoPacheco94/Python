from tabuleiro import opcoes, batalha_naval

placar_geral = 0
linha = None
coluna = None


print('BATALHA NAVAL')
print('Informe a posição do alvo')
print('Linha entre 0-4 e coluna entre 0-3')

for jogada in range(1,6):
    print('\nTentativa', jogada)
    linha = int(input('Informe a linha:'))
    coluna = int(input('Informe a coluna:'))
    
    while linha > 4 or coluna > 3:#Esse bloco teste se os números estão no range
        print('Posição inválida. Tente novamente!\n')
        print('Linha entre 0-4 e coluna entre 0-3')
        linha = int(input('Informe a linha:'))
        coluna = int(input('Informe a coluna:'))
        
    if batalha_naval[linha][coluna] == '*':#Caso seja jogada válida, vai daqui pra baixo
        placar_geral += 10
        print(f'Linha:{linha} Coluna:{coluna}\n!... NO ALVO ...!\n')

            
    else:
        placar_geral -= 10
        print(f'Linha:{linha} Coluna:{coluna}\nTiro na água :(\n')
    
            
        
print('Sua pontuação final:',placar_geral)