from time import sleep


class Caneta:
    cor = None
    modelo = None
    qtd_tinta = 10
    
    def riscar(self):
        if self.qtd_tinta:#refere a propria classe | se a condição for zero vale false
            print('Estou riscando')
            self.qtd_tinta -= 1
        else:
            print('Caneta sem tinta')


caneta_a = Caneta() # caneta_a a é um objeto (instancia) da classe caneta
caneta_a.cor = 'vermelha'
caneta_a.modelo = 'Quadro Branco'

print(caneta_a.cor)
print(caneta_a.qtd_tinta)

for i in range(0,13):
    caneta_a.riscar()
    sleep(3)
    print(f'Nível de tinta: {caneta_a.qtd_tinta}\n')
    sleep(1)

print(f'Nível de tinha atual: {caneta_a.qtd_tinta}')

#####################################################################

caneta_b = Caneta()
caneta_b.cor = 'Azul'
caneta_b.modelo = 'Quadro branco'

print(f'Status caneta {caneta_b.modelo} cor {caneta_b.cor}')
print(f'Nível atual de tinta: {caneta_b.qtd_tinta}')

for i in range (0,12):
    caneta_b.riscar()
    print(f'Nível de tinta: {caneta_b.qtd_tinta}\n')
    sleep(2)
print(f'Nível de tinta: {caneta_b.qtd_tinta}')

