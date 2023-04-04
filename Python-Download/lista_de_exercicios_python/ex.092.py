from datetime import date
carteira = dict()
while True:
    carteira['Nome'] = str(input('Nome: ')).title() .strip()
    data = int(input('Ano de nascimento: '))
    carteira['Idade'] = date.today().year - data
    carteira['Carteira de Trabalho'] = int(input('Carteira de trabalho[0 = não tem]: '))
    if carteira['Carteira de Trabalho'] == 0:
        break
    else:
        carteira['Contrataçao'] = int(input('Ano de contratação: '))
        carteira['Salário'] = float(input('Salário: '))
        carteira['Aposentadoria'] = 65 - carteira['Idade']
        break
print('-=' * 30)
for k, v in carteira.items():
    print(f'{k} tem o valor: {v}')
