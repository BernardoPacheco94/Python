from time import sleep
from pessoas import Pessoa   

pessoa_1 = Pessoa()
pessoa_1.nome = 'Daniel Orivaldo da Silva'
pessoa_1.data_nascimento = '31/12/1984'
pessoa_1.funcao_profissional = 'Manobrista'
pessoa_1.email = 'galocego@5reais.com'
pessoa_1.telefone = '55991919191'

pessoa_2 = Pessoa()
pessoa_2.nome = 'Ronaldo Nazario'
pessoa_2.data_nascimento = '25/03/2000'
pessoa_2.funcao_profissional = 'Programador'
pessoa_2.email  = 'ronaldo_dev@github.com'
pessoa_2.telefone = '21999191954'

pessoa_3 = Pessoa()
pessoa_3.nome = 'Jeremias'
pessoa_3.data_nascimento = '25/03/1999'
pessoa_3.funcao_profissional = 'Bebado'
pessoa_3.email  = 'sememail@null.com'
pessoa_3.telefone = '21999191954'

pessoas = []
pessoas.append(pessoa_1)
pessoas.append(pessoa_2)
pessoas.append(pessoa_3)


print(30*'-')
print('Cartão de Visitas\n')
print('1) Cadastrar')
print('2) Imprimir todos os cartões')
print('3) Sair')
print(30*'-')

op = int(input('Digite opção'))

while op != 3:

    if op == 1:
        pessoa = Pessoa()
        pessoa.criar_cadastro()
        pessoas.append(pessoa)
        op = 0
    
    elif op == 2:
        for pessoa in pessoas:
            pessoa.criar_cartao()
            sleep(1)
        sleep(3)
        op = 0
        
    else:
        print('----------------------------')
        print('1) Cadastrar')
        print('2) Imprimir todos os cartões')
        print('3) Sair')
        op = int(input('Digite opção:'))

print('Encerrando sistema.')
sleep(3)
    
