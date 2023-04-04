from time import sleep
from ex115.lib.interface import *
from ex115.lib.arquivo import *

arq = 'cursoemvideo.txt'

if not arqExiste(arq):
    criararq(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sitema'])
    if resposta == 1:
        lerarquivo(arq)
    elif resposta == 2:
        inicio('NOVO CADASTRO')
        nome = str(input('Nome: ')).title()
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        inicio('\033[32mSaindo do Programa... Volte sempre!\033[m')
        break
    else:
        inicio('\033[31mERRO. Digite uma opção válida!\033[m')
    sleep(2)
