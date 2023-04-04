print('-=-' * 14)
nota1 = float(input('Digite a sua nota do primeiro semestre: '))
nota2 = float(input('Digite a sua nota do segundo semestre: '))
print('-=-' * 14)
soma = (nota1 + nota2) / 2
if soma < 50:
    print('Com a nota de {}, você foi \033[31mREPROVADO!\033[m'.format(soma))
elif soma > 50 and soma < 69:
    print('A sua média foi {}, você ficou de \033[36mRECUPERAÇÃO!\033[m'.format(soma))
elif soma > 70:
    print('Párabens! Sua média foi de {}, você foi \033[32mAPROVADO!\033[m'.format(soma))
