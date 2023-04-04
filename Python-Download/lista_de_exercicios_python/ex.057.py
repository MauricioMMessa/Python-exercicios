sexo = ''
while sexo != 'F' and sexo != 'M':
    sexo = input('Digite seu gênero[F / M]: ') .upper()
    if sexo != 'F' and sexo != 'M':
        print('Digite um gênero valido!')

if sexo == 'F':
    print('Seja Bem Vinda!!!')
elif sexo == 'M':
    print('Seja Bem Vindo!')
