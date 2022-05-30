#gerando numeros aleatorios
from random import randint

nr_sorteado = randint(1, 60)
print(nr_sorteado)

print(20*'-')

#gerando randomicos a partir de uma lista
alunos = ['bernardo', 'marcelo', 'lorenzo', 'julia', 'pablo', 'matheus', 'padoin', 'victor', 'davi']

from random import choice
sorteado = choice(alunos)
print(sorteado)