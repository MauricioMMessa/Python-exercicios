salario = float(input('Qual seu salário atual? Digite aqui:R$'))
if salario > 1250:
    aumento1 = (salario / 100 * 10) + salario
    print('Seu salário atual com 10% de aumento é {:.2f}R$!'.format(aumento1))
else:
    aumento2 = (salario / 100 * 15) + salario
    print('Seu salário atual com 15% de aumento é {:.2f}R$'.format(aumento2))