palavras = ('guanabara', 'viado', 'de', 'mais')
print(f'As vogais da palavra', end='')
print()
for palavra in palavras:
    print(f'{palavra.upper()} são: ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
    print()
