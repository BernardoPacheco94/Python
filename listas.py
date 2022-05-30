alunos = ['Eduardo','Maiquel','Raphael','Lorenzo']
def linha ():
    print(30*'-')    


print('Lista:',alunos)
print('Ultimo indice:',alunos[-1]) #o menos seleciona o último elemento
linha()

print('Substituindo valor:')
alunos [2] = 'Bernardo'
print('Nova lista:',alunos)
linha()

print('Inserindo novo elemento:')
alunos.append('Julia')
print('Nova lista:',alunos)
linha()

print('Quantidade de itens:',len(alunos))
linha()

print('Quantidade de "Maiquel" na lista:',alunos.count('Maiquel'))
linha()

print('Lista em ordem alfabética:', sorted(alunos))# de tras pra frente, usaria o 'sorted(alunos, reverse=true)' - nao alterando a lista 
print('Lista em ordem alfabética:', alunos.sort)# altera a variavel lista para a ordem solicitada
linha()

inteiros = [2, 8, 9, 1, 14]
print('Menor valor da lista:',min(inteiros))
print('Maior valor da lista:',max(inteiros))
linha()

print('Pegando alguns elementos da lista', alunos[0:3])# pega até o índice 2
print('Pegando alguns elementos da lista, até o final', alunos[2:])
linha()

lista_range = range(0,11)
print(lista_range)
print(lista_range[2])