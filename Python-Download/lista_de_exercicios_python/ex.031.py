km = int(input('Quantos km é até seu destino? '))
if km < 201:
    soma = float(km * 0.50)
    print('O valor da sua passagem é de {:.2f}R$'.format(soma))
else:
    soma2 = float(km * 0.45)
    print('O valor da sua passagem é de {:.2f}R$'.format(soma2))