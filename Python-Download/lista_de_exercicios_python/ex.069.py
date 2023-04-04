muie20 = 0
maior = 0
homi = 0
while True:
    print('Lista de Cadastro'.center(50))
    nome = str(input('Digite o nome da pessoa: ')).strip() .title()
    idade = int(input('Digite a idade da pessoa: '))
    sexo = str(input('Digite o sexo da pessoa: ')).strip() .lower()
    #maiores de 18 anos
    if idade > 18:
        maior += 1
    #homens cadastrados
    if sexo == 'masculino':
        homi += 1
    #mulheres que tem menos de 20 anos
    if sexo == 'feminino' and idade < 20:
        muie20 += 1
    escolha = str(input('Deseja continuar?[S/N]: ')).strip().upper()
    if escolha == 'N':
        break
print(f'{maior} Pessoas tem mais de 18 anos!')
print(f'{homi} Homens foram cadastrados!')
print(f'{muie20} Mulheres tem menos de 20 anos!')