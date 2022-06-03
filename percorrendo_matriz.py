matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
soma_col_0 = 0
soma_col_1 = 0
soma_col_2 = 0

for indice_linha in range(0,3):
    for indice_coluna in range(0,3):
        print(f'Linha: {indice_linha} Coluna: {indice_coluna} -> Valor: {matriz[indice_linha][indice_coluna]}')
        if (matriz[indice_linha][indice_coluna] % 2) == 0:
            print(f'{matriz[indice_linha][indice_coluna]} é Par')
        else:
            print(f'{matriz[indice_linha][indice_coluna]} é Ímpar')
        
        #somando os valores de cada coluna
        if indice_coluna == 0:
            soma_col_0 += matriz[indice_linha][indice_coluna]
        elif indice_coluna == 1:
            soma_col_1 += matriz[indice_linha][indice_coluna]
        elif indice_coluna == 2:
            soma_col_2 += matriz[indice_linha][indice_coluna]
            
print(f'Soma da coluna 0: {soma_col_0}')
print(f'Soma da coluna 1: {soma_col_1}')
print(f'Soma da coluna 2: {soma_col_2}')