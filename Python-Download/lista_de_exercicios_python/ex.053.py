print('-=' * 25)
print('Digite algo para saber se é uma palavra palindroma')
print('-=' * 25)
p = input('Digite algo: ').strip() .replace(' ',  '') .lower()
if p [::-1] == p:
    print('A palvra é palindroma!')
else:
    print('A palavra não é palindroma!')
