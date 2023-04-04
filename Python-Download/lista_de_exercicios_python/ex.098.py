from time import sleep


def contador(i, f, p):
        if p < 0:
            p *= -1
        if p == 0:
            p = 1

        print('_' * 50)
        print(f'Contagem começando de {i} até {f}. Pulando de {p} em {p}!')

        if i < f:
            cont = i
            while cont <= f:
                print(f'{cont} ', end='')
                sleep(0.3)
                cont += p
            print('FIM')
            print('_' * 50)
        else:
            cont = i
            while cont >= f:
                print(f'{cont} ', end='')
                sleep(0.3)
                cont -= p
            print('FIM')
            print('_' * 50)
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem')
ini = int(input('Inicio: '))
fin = int(input('Fim: '))
pul = int(input('Passo: '))
contador(ini, fin, pul)
