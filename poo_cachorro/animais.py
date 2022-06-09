class Cachorro:
    nome = None
    raca = None
    tamanho = None
    pelo = None
    status = 'ACORDADO'
    
    def escrever_quem_sou(self):
        print(f'Meu nome é {self.nome}, sou da raça {self.raca} e estou: {self.status.title()}. \n')
    
    
    def dormir(self):
        if self.status == 'ACORDADO':
            self.status = 'DORMINDO'
            print('Agora vou... zzZZZzzzzZZzzZZz!\n')
        else:
            print('zzZZZzzzzZZzzZZz!\n')
    
    
    def acordar(self):
        if self.status == 'DORMINDO':
            self.status = 'ACORDADO'
            print('Acordei!\n')
        else:
            print('já estou acordado!\n')
    
    def comer(self):
        if self.status == 'ACORDADO':
            print('HMMMMMM... NHAM NHAM\n')
        else:
            print('to não men zzZZZzzzzZZzzZZz!\n')
            
    def correr(self):
        if self.status == 'ACORDADO':
            print('vruuuuuummmmm\n')
        else:
            print('to não men zzZZZzzzzZZzzZZz!\n')
            
    def latir(self):
        if self.status == 'ACORDADO':
            print('auuuuuuuuuuuuuuuuu uuuu uuuuuu\n')
        else:
            print('to não men zzZZZzzzzZZzzZZz!\n')