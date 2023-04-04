import random
a1 = str(input('Nome do Aluno: '))
a2 = str(input('Nome do Aluno: '))
a3 = str(input('Nome do Aluno: '))
a4 = str(input('Nome do Aluno'))
lista = [a1, a2, a3, a4]
a = random.choice(lista)
print("Os alunos são: {}, {}, {} e {}.\nE o sorteado é: {}!".format(a1, a2, a3, a4, a))
