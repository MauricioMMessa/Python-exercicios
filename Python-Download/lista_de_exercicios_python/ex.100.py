from random import randint
from time import sleep
lista = list()


def sorteia(list):
    print('<->' * 15)
    print('Sorteando os números...')
    sleep(0.4)
    for cont in range(0, 5):
        num = randint(1, 9)
        list.append(num)
        print(num, end=' ')
        sleep(0.3)
    print()
    print('PRONTO')
    print('<->' * 15)


def somapar(list):
    print('<->' * 15)
    print(f'Somando os pares de {list}...')
    sleep(2)
    pares = 0
    for n in list:
        if n % 2 == 0:
            pares += n
    print(f'A soma dos pares é {pares}.')
    print('<->' * 15)


sorteia(lista)
somapar(lista)
