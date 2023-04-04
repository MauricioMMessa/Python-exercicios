print('-=' * 19)
print('Somente números pares serão somados!')
print('-=' * 19)
soma = 0
for c in range(0, 6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        soma += n
print(f'O resultado da soma dos pares é {soma}!')
