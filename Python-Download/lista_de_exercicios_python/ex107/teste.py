# métodoGuanabara
import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(p, 10)}')
print(f'Diminuindo 10%, temos R${moeda.diminuir(p, 15)}')

# my metodo
'''import moeda
numer = float(input('Digite um número >'))
moeda.moeda(numer)'''
