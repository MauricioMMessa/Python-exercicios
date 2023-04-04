lista = list()
contador = 0
contador5 = 0
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    contador += 1
    opcao = input('Deseja continuar?[S/N] ').upper() .strip()

    while opcao not in 'SsNn':
        print('Digite [\033[31mS ou N\033[m] para continuar!')
        opcao = input('Deseja continuar?[S/N] ').upper() .strip()
        if opcao in 'NnSs':
            break
    if opcao == 'N':
        break

print(f'Foram digitados {contador} numeros!')
lista.sort(reverse=True)
print(f'Os valores da lista em ordem decrescente são {lista}!')
if 5 in lista:
    print(f'O número 5 está na lista!')
else:
    print('O número 5 não foi digitado!')
