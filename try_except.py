"""try:
    #Digitar entrada inválida
    numero = int(input('Digite um número:'))
    print(f'O dobro de {numero} é {numero*2}')
except:
    print('Você precisa digitar um número!')
"""
try:
    numero_1 = int(input('Digite o primeiro número:'))
    numero_2 = int(input('Digite o segundo número:'))
    print (f'{numero_1} / {numero_2} = {numero_1 / numero_2}')

except ZeroDivisionError:#Específico para exceção de divisão por zero
    print('Impossível dividir por ZERO')

except:
    print (f'Não foi possível efetuar divisão')#Qualquer outra exceção
else: #Entra sempre que não entra em exceção nenhuma
    print('Programa executado corretamente! GG')
finally:#Executa sempre, independente de ter exceção ou não
    print('FIM')