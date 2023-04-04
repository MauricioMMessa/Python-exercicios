velocidade = int(input('A qual velocidade você esta dirigindo? '))
if velocidade >= 81:
    print('Você foi multado!')
    multa = (velocidade - 80) * 7
    print('Sua multa foi de {:.2f}R$! Dirija mais devagar na proxima vez!'.format(multa))
else:
    print('Continue sem ultrapassar 80km/h!')
