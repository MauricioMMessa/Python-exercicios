from random import choice
from time import sleep

print('\033[36;40m-=-\033[m' * 11)
print('\033[36;40mMinigame Pedra, Papel e Tesoura  \033[m')
print('\033[36;40m-=-\033[m' * 11)
opcoes = ('pedra', 'papel', 'tesoura')
while True:
    jogador = input('Escolha: Pedra, Papel, ou Tesoura: ').lower()
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('POO!!!')
    computador = choice(opcoes)
    if jogador == computador:
        print('Empate!')
    elif jogador == 'pedra' and computador == 'papel':
        print('\033[31mVocê perdeu! O computador escolheu papel!')
    elif jogador == 'papel' and computador == 'tesoura':
        print('\033[31mVocê perdeu! O computador escolheu tesoura!')
    elif jogador == 'tesoura' and computador == 'pedra':
        print('\033[31mVocê perdeu! O computador escolheu pedra!\033[m')
    else:
        print('\033[32mVocê ganhou! O computador escolheu {}!'.format(computador))

    continuar = input("\033[32mDeseja jogar novamente?\033[m (s/n) ").lower()
    if continuar.lower() != "s":
        break

print('Obrigado por jogar! Foi divertido!!! :)')
