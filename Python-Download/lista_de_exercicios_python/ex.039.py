from datetime import date
print('-=-' * 10)
ano = int(input('Qual o ano do seu nascimento? '))
idade = date.today().year - ano

if idade < 18:
    falta = 18 - idade
    print('Faltam ainda, {} anos pra você se alistar ao exercito!'.format(falta))
elif idade == 18:
    print('Você fez ou faz 18 anos esse ano! Está na hora de se alistar!')
elif idade > 18:
    passou = idade - 18
    print('Já passou {} anos desde o seu alistamento!'.format(passou))
