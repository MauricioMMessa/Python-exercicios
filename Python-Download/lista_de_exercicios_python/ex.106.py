from time import sleep
c = ('\033[m',       # 0-sem cor
     '\033[30;47m',  # 1-branco
     '\033[30;41m',  # 2-vermelho
     '\033[30;42m',  # 3-verde
     '\033[30;44m',  # 4-azul
     '\033[30;45m')  # 5-roxo


def ajuda(com):
    titulo(f'Acessando o Manual do comando \'{comando}\'', 4)
    print(c[1], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


while True:
    titulo('SISTEMA DE AJUDA PyHELP', 3)
    comando = str(input('Função ou Biblioteca >'))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 2)
