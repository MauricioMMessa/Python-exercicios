from random import randint
from time import sleep
vitoria = 0
while True:
    pi = ' '
    while pi not in 'PI':
        pi = str(input('Você quer par ou ímpar?[P / I] ')).strip() .upper()
    n = int(input('Digite um número de 0 a 10: '))
    sleep(0.5)
    comp = randint(1, 2)
    soma = n + comp
    if pi == 'P' and soma % 2 == 0:
        print('Parabens você ganhou!')
        vitoria += 1
    elif pi == 'I' and soma % 2 == 1:
        print('Parabéns você ganhou!')
        vitoria += 1
    else:
        print('Você Perdeu!')
        break
print(f'Você ganhou {vitoria} vezes!' if vitoria > 1 else f'Voce ganhou {vitoria} vez!')
