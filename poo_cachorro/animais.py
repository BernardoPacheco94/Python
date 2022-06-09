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
            print('Agora vou... zzZZZzzzzZZzzZZz!')
        else:
            print('zzZZZzzzzZZzzZZz!')
    
    
    def acordar(self):
        if self.status == 'DORMINDO':
            self.status = 'ACORDADO'
            print('Acordei!')
        else:
            print('já estou acordado!')