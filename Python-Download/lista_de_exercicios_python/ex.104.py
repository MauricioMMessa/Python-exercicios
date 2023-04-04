def leiaInt(num):
    ok = False
    valor = 0
    while True:
        n = str(input(num))
        if n.isnumeric():
            ok = True
            valor = int(n)
        else:
            print('\033[31mERRO. Digite um número inteiro VÁLIDO!!!\033[m')
        if ok:
            break
    return valor


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
