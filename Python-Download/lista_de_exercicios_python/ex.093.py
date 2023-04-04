partidas = list()
jogador = dict()
jogador['nome'] = str(input('Nome: ')).strip() .title()
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for c in range(1, tot + 1):
    partidas.append(int(input(f'Quantos gols na partida {c}? ')))

jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)

print('-=' * 30)
print(jogador)
print('-=' * 30)

for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')

print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas!')

for i, v in enumerate(jogador["gols"]):
    print(f'    => Na partida {i + 1}, ele fez {v} gols!')

print(f'Total de {jogador["total"]} gols!')
