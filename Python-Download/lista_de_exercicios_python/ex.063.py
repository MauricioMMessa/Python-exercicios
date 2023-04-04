n = int(input('Digite um número para descobrir a sequência de Fibonacci: '))
f = [0, 1]
i = 2
while i < n:
    termoatual = f[i-1] + f[i-2]
    f.append(termoatual)
    i += 1
print(f)

'''print('Codigo do guanabara')
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('{} - {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' - {}.format(t3), end='')
    t1 = t2
    t2 =t3
    cont += 1
print(FIM)'''