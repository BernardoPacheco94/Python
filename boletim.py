print ('BOLETIM FINAL')

n1 = float(input('Digite a nota 1:'))
n2 = float(input('Digite a nota 2:'))
n3 = float(input('Digite a nota 3:'))

media = (n1+n2+n3)/3

if not(media<0 or media>10):
    print('Media final: ',round(media,2))
    
    if media >= 6:
        print('Aluno aprovado')
    else:
        print('Aluno reprovado')
else:
    print('Média',round(media,2),'inválida, verifique valores informados')
    