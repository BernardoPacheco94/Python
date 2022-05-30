def linha():
    print(30*'-')


lista = range(0,11)

for item in lista:
    print(item,'ao quadrado é:',item**2)
print ('Fim do for')
linha()


alunos = ['bernardo', 'maiquel', 'xaranai','augusto']

for aluno in sorted(alunos):
    print(aluno.title())
linha()
