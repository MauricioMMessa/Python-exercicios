print('\033[36;40m-=-\033[m' * 28)
print('\033[36;40mIrei calcular seu IMC(Índice de Gordura Corporal)! Digite seu peso e altura abaixo! \033[m')
print('\033[36;40m-=-\033[m' * 28)
altura = float(input('Sua altura: '))
peso = float(input('Seu peso: '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Seu IMC foi: \033[34m{:.1f}, Abaixo do Peso!'.format(imc))
elif imc > 18.5 and imc < 25:
    print('Seu IMC foi: \033[32m{:.1f}, Peso Ideal!'.format(imc))
elif imc > 25 and imc < 30:
    print('Seu IMC foi: \033[33m{:.1f}, Sobrepeso!'.format(imc))
elif imc > 30 and imc < 40:
    print('Seu IMC foi: \033[31m{:.1f}, Obsidade!'.format(imc))
else:
    print('Seu IMC foi: \033[4;31m{:.1f}, Obsidade Mórbida!'.format(imc))