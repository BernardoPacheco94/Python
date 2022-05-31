print('ADIVINHE O NÚMERO')

from random import randint
n_sorteado = randint(1,10)

nivel = input('Informe o nivel [F] para fácil e [D] para difícil')

while nivel.upper() != 'D' and nivel.upper() != 'F':
    print(f'{nivel} - Opção Inválida, tente novamente')
    nivel = input('Informe o nivel [F] para fácil e [D] para difícil')

if nivel.upper() == 'F':
    chances = 5
elif nivel.upper() == 'D':
    chances = 2
else:
    print(f'{nivel.upper()}: Nivel inválido')
    exit()

for i in range(1,chances+1):
    chute = int(input(f'{i}a Chance:'))
    if(chute == n_sorteado):
        print(f'Você acertou, o número sorteado é: {n_sorteado}')   
        exit()
    else:
        if i == chances:
            msg = 'Inicie um novo jogo'
        else:
            msg = 'Tente novamente'
        print(f'Você errou. {msg}')
print(f'O número era: {n_sorteado}')