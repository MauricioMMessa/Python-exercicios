import math
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
h = math.sqrt((co**2) + (ca**2))
print('O valor da Hipotenusa é: {:.1f}'.format(h))
