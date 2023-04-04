lista = list()

while True:
    n1 = int(input('Digite um valor: '))
    if n1 in lista:
        print('Valor duplicado!')
    else:
        print('Valor adicionado!')
        lista.append(n1)

    opcao = input('Deseja adicionar mais valores? [S/N] ').upper() .strip()
    while opcao not in 'SN':
        print('Erro INVALIDO!')
        op = input('Deseja adicionar mais valores? [S/N] ').upper() .strip()
        if op in 'NnSs':
            break
    if opcao == 'N':
        break

lista.sort()
print(lista)
