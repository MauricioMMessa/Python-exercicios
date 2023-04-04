print('{:~^40}'.format(' MESSA MARKET '))
preco = float(input('Preço da compra: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] A vista no dinheiro/cheque
[ 2 ] A vista no cartão
[ 3 ] Parcelado em até 2x no cartão
[ 4 ] Parcelado em 3x ou mais no cartão''')
opcao = int(input('Digite a opção de pagamento: '))

if opcao == 1:
    soma = preco - (preco / 100 * 10)
elif opcao == 2:
    soma = preco - (preco / 100 * 5)
elif opcao == 3:
    soma = preco
    parcela = preco / 2
    print('A sua parcela vai ser: 2x de R${}'.format(parcela))
elif opcao == 4:
    soma = preco + (preco / 100 * 20)
    total = int(input('Quantas parcelas: '))
    parcela = soma / total
    print('A sua parcela vai ser: {}x de R${} COM JUROS'.format(total, parcela))
else:
    print('\033[31mERRO! Selecione uma forma válida de pagamento!\033[m')
    soma = preco
print('O valor da sua compra é R${:.2f} e no final vai ficar por R${:.2f}'.format(preco, soma))