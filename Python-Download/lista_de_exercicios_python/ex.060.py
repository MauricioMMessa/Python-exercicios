from time import sleep
n = int(input('Digite um número: '))
if n < 0:
    print('ERRO. Não da pra fazer fatorial com número negativo!')
else:
    multi = 1
    print('Calculando o fatorial de {}:'.format(n))
    sleep(0.5)
    for c in range (1, n + 1):
        multi *= c
        print(c, end='')
        if c < n:
            print(' x ', end='')
        else:
            print(' = ', end='')
    print(multi)
