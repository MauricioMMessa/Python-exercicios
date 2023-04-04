lista = []
listai = []
listap = []

while True:
    n = int(input('Digite um número: '))
    lista.append(n)

    if n % 2 == 0:
        listap.append(n)
    else:
        listai.append(n)
    escolha = input('Deseja continuar? [S/N]').upper() .strip()

    while escolha not in 'SN':
        print('\033[31mInvalido\033[m')
        escolha = input('Deseja continuar? [S/N]').upper().strip()
        if escolha in 'SN':
            break
    if escolha == 'N':
        break

print(f'A lista completa é {lista}')
print(f'A lista dos números pares é {listap}')
print(f'A lista com números impares é {listai}')
