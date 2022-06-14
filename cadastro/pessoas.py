from datetime import datetime, date

class Pessoa:
    nome: None
    data_nascimento: None
    funcao_profissional: None
    email: None
    telefone: None

    def calcular_idade(self):
        data_atual = datetime.now()
        self.data_nascimento = datetime.strptime(self.data_nascimento, '%d/%m/%Y').date()
        idade = (data_atual.date()-self.data_nascimento)/365
        self.data_nascimento = self.data_nascimento.strftime('%d/%m/%Y')#correcao para poder fazer o loop
        return idade.days
    
    def criar_cartao(self):
        print(30*'-')
        print('Nome:',self.nome)
        print('Idade:',self.calcular_idade(),'anos')
        print('Função:',self.funcao_profissional)
        print('E-mail:',self.email)
        print('Telefone:',self.telefone)
        print(30*'-')
        
        
    def criar_cadastro(self):
        self.nome = input('Informe seu nome e sobrenome:')
        self.data_nascimento = input('Data de Nascimento (dd/mm/aaaa):')
        self.funcao_profissional = input('Profissão:')
        self.email = input('Email:')
        self.telefone = input('telefone:')
    
 
