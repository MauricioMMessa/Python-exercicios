lista = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    esc = str(input('Acrescentar mais alunos?[S/N]: ')).strip() .upper()
    while esc not in 'SN':
        print('\033[31mOpção Invalida\033[m')
        esc = str(input('Acrescentar mais alunos?[S/N]: ')).strip().upper()
        if esc in 'SN':
            break
    if esc == 'N':
        break
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
for v, c in enumerate(lista):
    print(f'{v:<4}{c[0]:<10}{c[2]:>8.1f}')
while True:
    mos = int(input('Mostrar nota de qual aluno?[999 para encerrar] '))
    if mos == 999:
        break
    if mos < len(lista):
        print(f'As notas de {lista[mos][0]} é {lista[mos][1]}')
