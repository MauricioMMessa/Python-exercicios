print('\033[31m-=-\033[m' * 17)
print('Digite um número que você quer converter abaixo.')
print('\033[31m-=-\033[m' * 17)
numero = int(input('Digite um número para ser convertido: '))
print(
    'Para converter em Binário: \033[4mDigite 1.\033[m || Para converter em Octal: \033[4mDigite 2.\033[m || Para '
    'converter em Hexadecimal:'
    ' \033[4mDigite 3.\033[m')
escolha = int(input('Digite o número para conversão escolhido: '))
if escolha == 1:
    binario = bin(numero)[2:]
    print('\033[31m-=-\033[m' * 23)
    print('O número escolhido foi {}, e a conversão dele para binário é {}!'.format(numero, binario))
    print('\033[31m-=-\033[m' * 23)
elif escolha == 2:
    octal = oct(numero)[2:]
    print('\033[31m-=-\033[m' * 23)
    print('O número escolhido foi {}, e a conversão dele em octal é {}!'.format(numero, octal))
    print('\033[31m-=-\033[m' * 23)
else:
    var = escolha == 3
    hexadecimal = hex(numero)[2:]
    print('\033[31m-=-\033[m' * 23)
    print('O número escolhido foi {}, e a conversão dele para hexadecimal é {}!'.format(numero, hexadecimal))
    print('\033[31m-=-\033[m' * 23)
    