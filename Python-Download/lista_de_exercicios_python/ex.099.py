from random import randint


def maior(numeros):
    print('-=' * 25)
    mai = contadorn = 0
    for enu, nu in enumerate(numeros):
        contadorn += 1
        print(nu, end=' ')
        if enu == 0:
            mai = nu
        else:
            if nu > mai:
                mai = nu
    print(f'Foram {contadorn} números ao todo.')
    print(f'O maior valor foi {mai}')


numero = list()
contador2 = 0
contador = 0
while contador2 < 4:
    alea = randint(1, 9)
    contador2 += 1
    while contador < alea:
        num = randint(1, 10)
        numero.append(num)
        contador += 1
    maior(numero[:])
    numero.clear()



#jeito do guanabara viado


'''def maior(* num):
    cont = maio = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='')
        if cont == 0:
            maio = valor
        else:
            if valor > maio:
                maio = valor
        cont += 1
    print(f'Foram informados {cont} valores.')
    print(f'O maior valor informado foi {maio}.')

maior(1, 5, 3, 5, 6, 2)
maior(6, 2, 5 ,7, 2)
maior(2, 5)
maior(5)
maior()'''