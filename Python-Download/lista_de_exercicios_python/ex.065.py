somav = soman = maior = menor = 0

while True:
    n = int(input('Digite um número: '))
    sn = str(input('Deseja continuar?[S/N] ')).strip() .upper()
    somav += n
    soman += 1

    if soman == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
        elif n == 0:
            menor = 0

    if sn == 'N':
        break
    elif sn == 'S':
        continue
    elif sn != 'S' or sn != 'N':
        print('\033[31mERRO!!! invalido!\033[m')
        break
print('O maior valor digitado é {}, e o menor {}!'.format(maior, menor))
print('A média dos números digitados é de {:.0f}!'.format(somav / soman))
