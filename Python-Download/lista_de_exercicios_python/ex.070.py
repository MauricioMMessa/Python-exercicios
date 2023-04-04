print('Loja do Dock´s'.center(50))
total = 0
mil = 0
caro = 0
nomec = ''
contagem = 0
while True:
    p = str(input('Qual o produto? '))
    preco = float(input('Qual o valor? '))
    escolha = ' '
    total += preco
    if preco > 1000:
        mil += 1
    contagem += 1
    if contagem == 1:
        caro = preco
        nomec = p
    if preco < caro:
        caro = preco
        nomec = p
    while escolha not in 'SN':
        escolha = str(input('Quer continuar?[S/N] ')).strip() .upper()
    if escolha == 'N':
        break
print(f'O total gasto na loja foi de {total :.2f}')
print(f'{mil} Produtos custa mais de 1000,00 reais!')
print(f'O nome do produto mais barato é {nomec}')
