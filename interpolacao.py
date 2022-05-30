#INTERPOLAÇÃO

nome = 'Jubileu'

print('Olá',nome,'seja bem-vindo!')

str_1 = 'Olá '+nome+' seja bem-vindo!'
print(str_1)

idade = 28
str_2 = 'Olá %s seja bem-vindo! Você tem %d anos' % (nome, idade)#%s -> string #d -> dual(numerico)
print(str_2)

str_3 = 'Olá {var_1} seja bem-vindo! Você tem {var_2} anos'.format(var_1=nome, var_2=idade)
print(str_3)

str_4 = f'Olá {nome} seja bem-vindo! Você tem {idade} anos'
print(str_4)