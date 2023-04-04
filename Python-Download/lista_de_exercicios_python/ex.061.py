t1 = int(input('Digite o primeiro termo da (PA): '))
r = int(input('Digite a RAZÃO: '))
ter = 10

i = 0
valoratual = t1

while ter > 0:
    print(valoratual)
    i += 1
    valoratual = t1 + r * i
    ter -= 1
