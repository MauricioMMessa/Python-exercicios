from random import randint
n1 = n2 = n3 = n4 = n5 = 0
for c in range(1):
    n1 = randint(1, 8)
    n2 = randint(1, 8)
    n3 = randint(1, 8)
    n4 = randint(1, 8)
    n5 = randint(1, 8)
tupla = (n1, n2, n3, n4, n5)
menor = min(tupla)
maior = max(tupla)
print(tupla)
print(f'O maior número sorteado é {maior}')
print(f'O menor número sorteado é {menor}')
