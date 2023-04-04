from random import randint
tentativas = 0
computador = 0
jogador = 0
print('---------------MINIGAME---------------')
print('Tente adivinhar um número de 0 a 10')
while True:
    computador = randint(1, 10)
    jogador = int(input('Digite seu palpite '))
    tentativas += 1
    if computador != jogador:
        print('O computador escolheu {}'.format(computador))
    else:
        print('Foram {} tentativas até acertar'.format(tentativas))
        break
print('Parabéns')
