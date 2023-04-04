midade = 0
nomevelho = 0
muie20 = 0
nomev = ''
for b in range(1, 5):
    nome = str(input('Digite o nome da {}º pessoa: '.format(b))).strip() .title()
    idade = int(input('Digite a idade da {}º pessoa: '.format(b)))
    sexo = str(input('Digite o sexo da {}º pessoa: '.format(b))).strip() .lower()
    #media de idade
    if idade > 0:
        midade += idade
    #nome do mais velho
    if b == 1 and sexo == 'masculino':
        nomevelho = idade
        nomev = nome
    else:
        if idade > nomevelho and sexo == 'masculino':
            nomevelho = idade
            nomev = nome
    #mulheres que tem menos de 20 anos
    if sexo == 'feminino' and idade < 20:
        muie20 += 1

print('A média de idade do grupo é {}'.format(midade / 4))
print('O nome e a idade do mais velho é {} {} anos!'.format(nomev, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos!'.format(muie20))
