n = int(input('Digite um número inteiro: '))
if n < 2:
    print('O número não é primo!')
else:
    primo = True
    for i in range(2, n):
        if n % i == 0:
            primo = False
    if primo:
        print('O número é primo!')
    else:
        print('O número não é primo!')
