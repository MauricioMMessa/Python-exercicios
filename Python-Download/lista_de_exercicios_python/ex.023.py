num = input('Escreva um número de 0 a 9999: ').strip()
s = '000' + num
print('Unidade: {}'.format(s[-1]))
print('Dezena: {}'.format(s[-2]))
print('Centena: {}'.format(s[-3]))
print('Milhar: {}'.format(s[-4]))
