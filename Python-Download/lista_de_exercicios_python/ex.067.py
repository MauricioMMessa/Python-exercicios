n = int(input('Digite o número que deseja saber a tabuada: '))
soma = 1
v = 1
while True:
    if n < 0:
        break
    else:
        for v in range(1, 11):
            print(n, ' x ', v, ' = ', n * v)
        print('~' * 15)
    if soma == 0:
        break
    n = int(input('Se quiser saber outro valor digite-o, Se não digite um valor negativo!: '))
print('cabo')
