print('CALCULADORA DE DESPESAS')
vl_hospedagem = float( input('Informe o valor da hospedagem por pessoa: '))
qtd_pessoas = int(input('Quantas pessoas estarão hospedadas?'))
qtd_pedagios = int(input('Informe quantos pedágios há no caminho'))
vl_pedagio = float(input('Qual o valor de cada pedagio?'))
autonomia = float(input('Informe a média em Km/l do veículo:'))
vl_combustivel = float(input('Informe o valor de 1L combustível'))
distancia = float(input('Quantos km até o destino?'))

vl_hospedagem_total = vl_hospedagem*qtd_pessoas
custo_pedagios = vl_pedagio*qtd_pedagios
consumo_total_combustivel = (distancia*2)/autonomia*vl_combustivel

custo_geral = vl_hospedagem_total+custo_pedagios+consumo_total_combustivel


print('DESPESAS: \n')
print('Despesas com hospedagem: R$', round(vl_hospedagem_total,2))
print('Despesas com pedágios: R$', round(custo_pedagios,2))
print('Despesas com combustível: R$', round(consumo_total_combustivel,2))
print('\nCUSTO GERAL DA VIAGEM: R$',round(custo_geral,2))