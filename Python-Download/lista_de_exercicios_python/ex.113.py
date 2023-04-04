def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31m]ERRO. Digite um número inteiro VÁLIDO!!!\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mUsuario preferiu não digitar esse valor!\033[m')
            return 0
        else:
            return n


def leiaFloat(num):
    while True:
        try:
            n = float(input(num))
        except (ValueError, TypeError):
            print('\033[31mERRO. Digite um número real VÁLIDO!!!\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mUsuario preferiu não digitar esse valor!\033[m')
            return 0
        else:
            return n


nI = leiaInt('Digite um número Inteiro: ')
nR = leiaFloat('Digite um número Real: ')
print(f'O valor inteiro digitado foi {nI} e o valor Real {nR}.')
