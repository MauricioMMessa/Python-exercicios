from datetime import date
maior = 0
menor = 0
for i in range(0, 7):
    ano = int(input('Digite o ano de nascimento: '))
    idade = date.today().year - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('{} Pessoas atingiram a maioridade!\n{} Pessoas ainda são menores!'.format(maior, menor))
