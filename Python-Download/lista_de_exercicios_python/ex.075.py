n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
n4 = int(input('Digite um número: '))
n5 = (n1, n2, n3, n4)
print(f'O número 9 apareceu {n5.count(9)} vezes')
if 3 in n5:
    print(f'O número 3 esta na {n5.index(3)+1}º posição')
else:
    print(f'Não possui o número 3!')
print('O número par é:', end=' ')
for c in range(0, len(n5)):
    if n5[c] % 2 == 0:
        print(n5[c], end=' ')
