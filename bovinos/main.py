from dados import bovinos

vacinacao_a = []
vacinacao_b = []

for bovino in bovinos:
    if bovino.get('peso_kg') >= 300:
        vacinacao_a.append(bovino)
    else:
        vacinacao_b.append(bovino)

print('VACINAÇÃO A')
for item in vacinacao_a:
    print(item.get('tipo'),item.get('peso_kg'))
print('----------------------')
print('VACINAÇÃO B')
for item in vacinacao_b:
    print(item.get('tipo'),item.get('peso_kg'))
