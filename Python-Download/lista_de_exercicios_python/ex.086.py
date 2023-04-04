#MeuCodigo....
mat = [[], [], []]
for c in range(0, 3):
    for v in range(0, 3):
        n1 = int(input(f'Digite um número para a posição [{c}|{v}]: '))
        mat[c].append(n1)
print('-=' * 15)
for b in mat:
    for n in b:
        print(f'[ {n:^5} ]', end='')
    print()
print('-=' * 15)

#codigoGuanabara....
'''matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
print('-=' * 30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()'''
