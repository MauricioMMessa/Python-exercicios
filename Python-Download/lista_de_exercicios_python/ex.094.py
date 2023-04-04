bololo = dict()
lista = list()
listam = list()
contador = media = 0

while True:
    bololo['nome'] = (str(input('Nome: ')).strip() .title())
    bololo['sexo'] = str(input('Sexo: [M|F]')).strip() .upper()

    while bololo['sexo'] not in 'MF':
        print('\033[31mERRO\033[m. Por favor, digite apenas \033[34mM\033[m ou \033[34mF\033[m!')
        bololo['sexo'] = str(input('Sexo: [M|F]')).strip().upper()
        if bololo['sexo'] in 'MF':
            break

    if bololo['sexo'] == 'F':
         listam.append(bololo['nome'])

    bololo['idade'] = int(input('Idade: '))
    media += bololo['idade']
    contador += 1
    lista.append(bololo.copy())
    bololo.clear()
    escolha = str(input('Deseja continuar? [S|N]')).strip() . upper()

    while escolha not in 'SN':
        print('\033[31mERRO\033[m. Por favor, digite apenas \033[34mS\033[m ou \033[34mN\033[m!')
        escolha = str(input('Deseja continuar? [S|N]')).strip() .upper()
        if escolha in 'SN':
            break

    if escolha == 'N':
        break

print(f'Ao todo temos {contador} pessoas cadastras!')
print(f'A média de idade é {media / len(lista):.2f}!')
print(f'As mulheres cadastradas foram {listam}')
print(f'LISTA DE PESSOAS QUE ESTÃO ACIMA DA MÉDIA:')

for c, v in enumerate(lista):
    if lista[c]['idade'] > media/len(lista):
        print(f'nome = , {v}')
