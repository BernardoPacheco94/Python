def entrar_inteiro():
    while True:
        try:
            return int(input('Digite um numero inteiro'))
        except:
            print('Não foi informado um número inteiro')

numero = entrar_inteiro()
print(f'O dobro de {numero} é {2*numero}')

"""
def entrar_inteiro():
    solicitar_inteiro = True
    while solicitar_inteiro:
        try:
            inteiro = int(input('Digite um numero inteiro'))
            solicitar_inteiro = False
            return inteiro
        except:
            # solicitar_inteiro = True - essa linha não é necessária, mas é o que ocorre no fulxo do código
            print('Não foi informado um número inteiro')

numero = entrar_inteiro()
print(f'O dobro de {numero} é {2*numero}')

"""