n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
m = 0
while True:
    m = int(input('----Menu----\n[1]SOMAR\n[2]MULTIPLICAR\n[3]MAIOR\n[4]NOVOS NÚMEROS\n[5]SAIR DO PROGRAMA\nESCOLHA: '))
    if m == 1:
        print('A soma dos valores é {}!'.format(n1 + n2))
    elif m == 2:
        print('A multiplicação dos valores é {}!'.format(n1 * n2))
    elif m == 3:
        if n1 > n2:
            print('O maior número é {}'.format(n1))
        else:
            print('O maior número é {}'.format(n2))
    elif m == 4:
        while m == 4:
            n1 = int(input('Digite um número: '))
            n2 = int(input('Digite um número: '))
            break
    else:
        print('Obrigado por usar nosso app!')
        break
