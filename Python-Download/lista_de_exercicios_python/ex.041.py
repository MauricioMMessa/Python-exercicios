from datetime import date
print('\033[31;40m-=-\033[m' * 26)
print('\033[31;40mDigite sua data de nascimento abaixo, e veja qual categoria você se encontra! \033[m')
print('\033[31;40m-=-\033[m' * 26)
ano = int(input('\033[4mDigite aqui o ano do seu nascimento:\033[m '))
idade = date.today().year - ano
if idade <= 9:
    print('Categoria: \033[32mMIRIM')
elif idade > 9 and idade < 15:
    print('Categoria: \033[32mINFANTIL')
elif idade > 13 and idade < 19:
    print('Categoria: \033[32mJUNIOR')
elif idade > 18 and idade < 21:
    print('Categoria: \033[32mSÊNIOR')
elif idade > 20:
    print('Categoria: \033[32mMASTER')

