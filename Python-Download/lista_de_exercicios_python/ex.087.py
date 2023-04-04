matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = soma3 = mai = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
print('-=' * 30)
for linha in range(0, 3):
    for coluna in range(0, 3):

        #Soma dos pares
        if matriz[linha][coluna] % 2 == 0:
            soma += matriz[linha][coluna]

        #soma da terceura coluna
        if coluna == 2:
            soma3 += matriz[linha][coluna]

        #Maior valor da segunda linha
        if linha == 1:
            mai = matriz[linha][coluna]
            if matriz[linha][coluna] > mai:
                mai = matriz[linha][coluna]

        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()

print(f'A soma de todos os pares digitados é {soma}')
print(f'A soma da terceira coluna é {soma3}')
print(f'O maior valor da segunda linha é {mai}')
