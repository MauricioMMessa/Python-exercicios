#n1 = int(input('Digite a nota do 1º semestre: '))
#n2 = int(input('Digite a nota do 2º semestre: '))
#soma = (n1 + n2)/2
#print('A sua média é: {}'.format(soma))

n1 = int(input('Digite a nota do 1º semestre: '))
n2 = int(input('Digite a nota do 2º semestre: '))
soma = (n1 + n2)/2
if soma >= 60:
    print('Parabéns! A sua média é: {}{}{}!'.format('\033[32m', soma, '\033[m'))
else:
    print('Precisa estudar mais! A sua média é: {}{}{}!'.format('\033[31m', soma, '\033[m'))
