nome = input('Nome do jogador: ').strip() .title()
gols = input('Gols marcados: ').strip()


def ficha(n, g):
    if n.isalpha():
        print(f'O jogador {n}, ', end='')
    else:
        print('O jogador <Desconhecido>, ', end='')
    if g.isnumeric():
        print(f'marcou {g} gol(s)!')
    else:
        print(f'marcou 0 gol(s)!')


ficha(nome, gols)
