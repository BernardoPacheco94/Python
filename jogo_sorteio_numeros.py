print('ADIVINHE O NÚMERO')

from random import randint
n_sorteado = randint(0,10)


for i in range(1,4):
    chute = int(input(f'{i}a Chance:'))
    if(chute == n_sorteado):
        print(f'Você acertou, o número sorteado é: {n_sorteado}')   
        exit()
    else:
        if i == 3:
            msg = 'Inicie um novo jogo'
        else:
            msg = 'Tente novamente'
        print(f'Você errou. {msg}')
print(f'O número era: {n_sorteado}')