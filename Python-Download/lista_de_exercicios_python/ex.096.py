def area(larg, comp):
    a = larg * comp
    print(f'A área do terreno {larg}x{comp} é {larg * comp}m²')


print(' Controle de Terrenos')
print('=' * 21)
l = float(input('Qual a largura do terreno? '))
c = float(input('Qual o comprimento? '))
area(l, c)
