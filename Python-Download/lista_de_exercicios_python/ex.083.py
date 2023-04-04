e = input('Digite uma expressão: ')
lista = list()

for c in e:
    if c == '(':
        lista.append('(')
    elif c == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break

if len(lista) == 0:
    print('A expressão está correta!')
else:
    print('A expressão está errada!')
''