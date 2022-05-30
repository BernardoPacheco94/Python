pessoas = []
total_pessoas = int(input('Quantas pessoas serão cadastradas?'))

while len(pessoas) < total_pessoas:#pessoas está em 0 e vai incremendar a cada cadastro
    pessoas.append(input('Informe nome:').title())
    
print('Listagem de pessoas:\n',sorted(pessoas))