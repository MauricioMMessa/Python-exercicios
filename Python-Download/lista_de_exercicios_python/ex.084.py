lista = list()
listal = list()
mai = men = 0

while True:
    listal.append(str(input('Nome: ')).strip() .title())
    listal.append(int(input('Peso[Kg]: ')))

    if len(lista) == 0:
        mai = men = listal[1]
    else:
        if listal[1] > mai:
            mai = listal[1]
        if listal[1] < men:
            men = listal[1]

    lista.append(listal[:])
    listal.clear()

    pergunta = str(input('Deseja continuar?[S/N] ')).strip() .upper()
    while pergunta not in 'SN':
        print('\033{31mERRO\033[m')
        pergunta = str(input('Deseja continuar?[S/N] ')).strip().upper()
        if pergunta in 'SN':
            break
    if pergunta == 'N':
        break

print(f'O total foi de {len(lista)} pessoas cadastradas!')
print(f'O maior peso foi de {mai}Kgs! Peso de', end='')
for p in lista:
    if p[1] == mai:
        print(f' ({p[0]})', end='')
print()
print(f'O menor peso foi de {men}Kgs! Peso de', end='')
for p in lista:
    if p[1] == men:
        print(f' ({p[0]})', end='')
print()
