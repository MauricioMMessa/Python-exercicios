print('\033[40m-=-\033[m' * 9)
print('\033[40mBem Vindo ao Banco Central \033[m')
print('\033[40m-=-\033[m' * 9)
nome = input('Qual seu nome?: ').strip() .title()
print('Ok Sr.{}, você quer um empréstimo para comprar uma casa!'.format(nome))
valorcasa = float(input('Qual o valor da casa? R$'))
salario = float(input('E qual o seu sálario? R$'))
anos = int(input('Em quantos anos pretende pagar? '))

pmensal = valorcasa / (anos * 12)
if pmensal > salario / 100 * 30:
    print('Infelizmente seu empréstimo foi negado Sr.{}, tente outro valor ou outras parcelas!'.format(nome))
else:
    print('Parábens Sr.{} seu empréstimo foi aprovado com parcelas de {:.2f}R$ mensal!'.format(nome, pmensal))
