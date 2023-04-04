from random import shuffle
a1 = str(input('Nome do aluno: '))
a2 = str(input('Nome do aluno: '))
a3 = str(input('Nome do aluno: '))
a4 = str(input('Nome do aluno: '))
lista = [a1, a2, a3, a4]
shuffle (lista)
print('A sequência para apresentar o trabalho sera:\n{}'.format(lista))
