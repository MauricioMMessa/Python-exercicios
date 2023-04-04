from time import sleep
from random import randint
from operator import itemgetter
jogador = dict()
ranking = list()
for c in range(1, 5):
    dado = randint(1, 6)
    jogador[f'jogador{c}'] = dado
print('-=' * 21)
print('Jogando o dado...')
sleep(0.5)

for k, v in jogador.items():
    print(f'{k} tirou {v} no dado')
    sleep(0.5)
ranking = sorted(jogador.items(), key=itemgetter(1), reverse=True)
print('-=' * 8, 'RANKING', '-=' * 8)
for k, v in enumerate(ranking):
    print(f'    {k + 1}º lugar: \033[32m{v[0]}\033[m tirou \033[32m{v[1]}\033[m no dado!')
