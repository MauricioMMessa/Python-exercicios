from random import randint
from time import sleep
jogos = list()
numeros = list()
quan = int(input('Quantos jogos você deseja gerar? '))
contador = 0
#para rodar os jogos que foi pedido
while quan != 0:
    #para sortear os números de 1 a 60
    while True:
        num = randint(1, 60)
        #para não ter repetições de numeros
        if num not in numeros:
            numeros.append(num)
        #o freio do primeiro while
        if len(numeros) >= 6:
            quan -= 1
            break
    #para adicionar a lista dentro da lista principal
    jogos.append(numeros[:])
    numeros.clear()
#para deixar cada lista em uma linha
print('-=' * 19)
print('\033[34mPreparando os Jogos...\033[m')
sleep(0.5)
for c in jogos:
    c.sort()
    contador += 1
    print(f'\033[32mJogo {contador}\033[m: {c}')
    sleep(0.3)
print('-=' * 6,'\033[32mBoa Sorte!!!\033[m','-=' * 6)
