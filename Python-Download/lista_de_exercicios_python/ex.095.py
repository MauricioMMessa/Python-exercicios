partidas = list()
jogador = dict()
time = list()
while True:
    jogador['nome'] = str(input('Nome: ')).strip() .title()
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    #O for é para rodar quantas partidas o usuario digitou
    for c in range(1, tot + 1):
        partidas.append(int(input(f'Quantos gols na partida {c}? ')))
    #Depois disso pega a lista q estava os gols e joga pro dicionario
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)  #E pega o total de gols que a soma foi feita na lista e joga pro dicionario tambem
    partidas.clear()
    opc = str(input('Deseja continuar? [S|N] ')).strip() .upper()
    time.append(jogador.copy())
    while opc not in 'SN':
        print('\033[31mERRO\033[m. Por favor, digite apenas \033[34mS\033[m ou \033[34mN\033[m!')
        opc = str(input('Deseja continuar? [S|N]')).strip() .upper()
        if opc in 'SN':
            break
    if opc == 'N':
        break

print('-=' * 50)
print('cod  ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 50)
for n, t in enumerate(time):
    print(f'{n:>4}  ', end='')
    for d in t.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 50)

while True:
    dados = int(input('Quer mostrar os dados de qual jogador? '))
    if dados == 999:
        break
    if dados >= len(time):
        print(f'ERRO! Não existe jogador com codigo {dados}!')
    else:
        print(f'Buscando dados do jogador {time[dados]["nome"]}:')
        for i, g in enumerate(time[dados]['gols']):
            print(f'   No jogo {i + 1} fez {g} gols!')
    print('-' * 40)
print('<< VOLTE SIEMPRE >>')

