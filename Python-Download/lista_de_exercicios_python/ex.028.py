from random import randint
comp = randint(0, 5)

usu = int(input('Tente adivinha um número de|0 a 5|. Boa sorte! '))
if comp == usu:
    print('Parabéns você ganhou! :)')
else:
    print('Mais sorte da próxima vez! :(')
print('O número sorteado foi {}'.format(comp))
