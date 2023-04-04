lista = []
lmaior = []
lmenor = []

for l in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {l}: ')))
menor = min(lista)
maior = max(lista)

for c, v in enumerate(lista):
    if v == maior:
        lmaior.append(c)
    elif v == menor:
        lmenor.append(c)

print(f'Os números digitados foram {lista}')
print(f'O maior número digitado é {maior} na posição {lmaior},e o menor {menor} na posição {lmenor}')
