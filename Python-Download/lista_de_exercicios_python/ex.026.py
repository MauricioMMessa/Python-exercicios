frase = input('Escreva uma frase: ').lower() .strip()
count = frase.count('a')
f1 = frase.find('a')+1
f2 = frase.rfind('a')+1
print('A letra "a" aparece {} vezes! A primeira na posição {}! e a ultima na posição {}!'.format(count, f1, f2))