'''lista = list()

for l in range(0,5):
    n = int(input('Digite um número: '))
    if l == 0:
        lista.append(n)

    if l == 1 and n > lista[0]:
        lista.append(n)
    elif l == 1 and n <= lista[0]:
        lista.insert(0, n)

    if l == 2 and n > lista[0] and n >= lista[1]:
        lista.append(n)
    elif l == 2 and n > lista[0] and n <= lista[1]:
        lista.insert(1, n)
    elif l == 2 and n <= lista[0]:
        lista.insert(0, n)

    if l == 3 and n >= lista[2]:
        lista.append(n)
    elif l == 3 and n > lista[0] and n <= lista[1]:
        lista.insert(1, n)
    elif l == 3 and n > lista[1] and n <= lista[2]:
        lista.insert(2, n)
    elif l == 3 and n <= lista[0]:
        lista.insert(0, n)

    if l == 4 and n >= lista[3]:
        lista.append(n)
    elif l == 4 and n > lista[0] and n <= lista[1]:
        lista.insert(1, n)
    elif l == 4 and n > lista[1] and n <= lista[2]:
        lista.insert(2, n)
    elif l == 4 and n > lista[2] and n <= lista[3]:
        lista.insert(3, n)
    elif l == 4 and n <= lista[0]:
        lista.insert(0, n)

print(lista)'''

#opção do Ives q tava bem mais facil!
lista = list()
for c in range(0, 5):
    n = int(input('digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print(f'adicionado na ultima posição')

    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'adicionado na posição {pos}')
                break
            pos += 1
print(lista)
