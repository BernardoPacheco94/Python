import os
from time import sleep

from ferramentas import soma, subtracao, multiplicacao, divisao
from menu import mostrar_menu, capturar_numeros
opcao = mostrar_menu()

while opcao != 5:
    
    nr_1, nr_2 = capturar_numeros()
    if opcao == 1:
        print(f'{nr_1} + {nr_2} = {soma(nr_1, nr_2)}')
        
    elif opcao == 2:
        print(f'{nr_1} - {nr_2} = {subtracao(nr_1, nr_2)}')
        
    elif opcao == 3:
        print(f'{nr_1} x {nr_2} = {multiplicaco(nr_1, nr_2)}')
        
    elif opcao == 4:
        print(f'{nr_1} ÷ {nr_2} = {divisao(nr_1, nr_2)}')
    
    else:
        print(f'Opção {opcao} não existe! Reiniciando calculadora!')
        
    sleep(4)
    os.system('clear')
    opcao = mostrar_menu()
    
print('Encerrando...')
    