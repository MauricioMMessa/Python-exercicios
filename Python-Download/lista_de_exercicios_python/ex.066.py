print('Digite um número qualquer para fazer a soma. Digite 999 para parar o programa!')
soma = 0
soma1 = 0
while True:
    n = int(input('Digite um número inteiro: '))
    if n == 999:
        break
    else:
        soma += n
        soma1 += 1
print('No total foram digitados {} números e a soma entre eles é {}!'.format(soma1, soma))
