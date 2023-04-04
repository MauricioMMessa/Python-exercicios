print('\033[1;31m~~~' * 25)
print('\033[4;32mDigite os valores das retas e descubra se é possivel formar um triângulo!\033[m')
print('\033[1;31m~~~\033[m' * 25)
a = int(input('Digite o tamanho da primeira reta: '))
b = int(input('Digite o tamanho da segunda reta '))
c = int(input('Digite o tamanho da terceira reta '))

if (b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
    print('Formou um triângulo!')
else:
    print('Não formou um triangulo!')
