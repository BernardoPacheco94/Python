matriz = [
        ['O', 'O', 'O'],
        ['O', 'X', 'X'],
        ['X', 'O', 'O'],
    ]
    
if (matriz [0][0] == 'X' and matriz [0][1] =='X' and matriz [0][2] =='X') or \
(matriz [1][0] == 'X' and matriz [1][1] =='X' and matriz [1][2] =='X') or \
(matriz [2][0] == 'X' and matriz [2][1] =='X' and matriz [2][2] =='X') or \
(matriz [0][0] == 'X' and matriz [1][0] =='X' and matriz [2][0] =='X') or \
(matriz [0][1] == 'X' and matriz [1][1] =='X' and matriz [2][1] =='X') or \
(matriz [0][2] == 'X' and matriz [1][2] =='X' and matriz [2][2] =='X') or \
(matriz [0][0] == 'X' and matriz [1][1] =='X' and matriz [2][2] =='X') or \
(matriz [0][2] == 'X' and matriz [1][1] =='X' and matriz [2][0] =='X'):
    print('X - Ganhou!')
    
elif (matriz [0][0] == 'O' and matriz [0][1] =='O' and matriz [0][2] =='O') or \
(matriz [1][0] == 'O' and matriz [1][1] =='O' and matriz [1][2] =='O') or \
(matriz [2][0] == 'O' and matriz [2][1] =='O' and matriz [2][2] =='O') or \
(matriz [0][0] == 'O' and matriz [1][0] =='O' and matriz [2][0] =='O') or \
(matriz [0][1] == 'O' and matriz [1][1] =='O' and matriz [2][1] =='O') or \
(matriz [0][2] == 'O' and matriz [1][2] =='O' and matriz [2][2] =='O') or \
(matriz [0][0] == 'O' and matriz [1][1] =='O' and matriz [2][2] =='O') or \
(matriz [0][2] == 'O' and matriz [1][1] =='O' and matriz [2][0] =='O'):
    print('O - Ganhou!')
else:
    print('Empate')