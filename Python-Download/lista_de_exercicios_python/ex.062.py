t1 = int(input('Digite o primeiro termo da (PA): '))
r = int(input('Digite a RAZÃO: '))
ter = int(input('Digite quantos termos deseja ver: '))

ter = ter
i = 0
valoratual = t1

while True:
    if ter > 0:
        print(valoratual)
        i += 1
        valoratual = t1 + r * i
        ter -= 1
        if ter == 0:
            ter = ter
            ter = int(input('Deseja ver mais termos? Para encerrar o programa digite[0]: '))

        if ter == 0:
            print('CABO!')
            break
