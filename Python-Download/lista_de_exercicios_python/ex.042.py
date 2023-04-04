print('\033[4;32mDigite os valores das retas e descubra se é possivel formar um triângulo!\033[m')
a = float(input('Digite o tamanho da primeira reta: '))
b = float(input('Digite o tamanho da segunda reta: '))
c = float(input('Digite o tamanho da terceira reta: '))
if a < b + c and b < a + c and c < a + b:
    print('As retas formaram um triângulo!')
    if a == b and a == c and b == c:
        print('O triângulo é Equilátero!')
    elif a == b != c or b == c != a or a == c != b:
        print('O triângulo é Isóceles!')
    else:
        print('O triângulo é Escaleno!')
else:
    print('As retas não formaram um triângulo!')