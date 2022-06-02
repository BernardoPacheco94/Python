from datetime import datetime

print('HOTELARIA')

tb_precos = {#aqui há uma lista dentro da outra
    'standard': {'adulto': 120, 'crianca': 60},# atencao às virgulas para separar os valores dentro de cada dict
    'luxo': {'adulto': 180, 'crianca': 90}
}

#entradas:
tipo_hospedagem = input('Informe o tipo de hospedagem:\n[standard] - [luxo]').lower()

qtd_adultos = int(input('Informe a quantidade de adultos:'))
qtd_criancas = int(input('Informe a quantidade de criancas:'))

checkin = datetime.strptime(input('Informe a data de checkin no formato DD/MM/AAA'), '%d/%m/%Y').date()#dois parametros, a entrada a ser convertida e o formato em que ela está, o .date() informa que necessito somente da data
checkout = datetime.strptime(input('Informe a data de checkout no formato DD/MM/AAA'), '%d/%m/%Y').date()
periodo = (checkout - checkin).days

valor_frigobar = float(input('Gastos com frigobar:'))

#calculos:
vl_total_adultos = qtd_adultos*periodo*tb_precos.get(tipo_hospedagem).get('adulto')
vl_total_criancas = qtd_criancas*periodo*tb_precos.get(tipo_hospedagem).get('crianca')

vl_total_hospedagem_pessoas = vl_total_adultos + vl_total_criancas

vl_total = vl_total_hospedagem_pessoas + valor_frigobar


#saídas:
print('*************** RELATÓRIO DA CONTA *******************')
print(f'Tipo de hospedagem: {tipo_hospedagem.upper()}')
print(f'Período da hospedagem: {periodo} dias')
print('**************************************************')
print(f'Quantidade de adultos: {qtd_adultos}')
print(f'Quantidade de crianças: {qtd_criancas}')
print(f'Valor total para adultos: R$ {round(vl_total_adultos, 2)}')
print(f'Valor total para crianças: R$ {round(vl_total_criancas,2)}')
print(f'Valor gasto em frigobar: R$ {round(valor_frigobar,2)}')
print('**************************************************')
print(f'VALOR TOTAL: R$ {vl_total}')
print('**************************************************')

forma_pgto = input('Pressione [V] para pagmento a vista ou [P] para pagamento a prazo').upper()
while forma_pgto != 'V' and forma_pgto != 'P':#Tratamento da entrada
    print(f'Forma de pagamento {forma_pgto} é inválida, tente novamente')
    forma_pgto = input('Pressione [V] para pagmento a vista ou [P] para pagamento a prazo').upper()
aliquota = 0
if forma_pgto == 'V':#setando aliquota do desconto
    aliquota = -(0.15)
else:
    aliquota = 0.05
vl_pgto_final = vl_total + vl_total * aliquota

print(f'VALOR FINAL DA CONTA: R$ {round(vl_pgto_final, 2)}')