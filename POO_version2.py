from time import sleep


class Caneta:

    def __init__ (self, cor=None, modelo=None):# None 
        self.cor = cor
        self.modelo = modelo
        self.qtd_tinta = 10
        
    
    def riscar(self):
        if self.qtd_tinta:#refere a propria classe | se a condição for zero vale false
            print('Estou riscando')
            self.qtd_tinta -= 1
        else:
            print('Caneta sem tinta')


caneta_a = Caneta(cor = 'vermelha', modelo = 'mdl')
print(caneta_a.cor)
print(f'Nível de tinta {caneta_a.qtd_tinta}')

caneta_a.riscar()
print('Nível de tinta:',caneta_a.qtd_tinta)


