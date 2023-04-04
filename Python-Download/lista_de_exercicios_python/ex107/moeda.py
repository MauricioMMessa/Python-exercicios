# métodoGuanabara
def aumentar(preco, taxa):
    res = preco + (preco * taxa/100)
    return res


def diminuir(preco, taxa):
    res = preco - (preco * taxa/100)
    return res


def dobro(preco):
    res = preco * 2
    return res


def metade(preco):
    res = preco / 2
    return res


# my metodo
'''def moeda(num=0):
    porcentage = 10 * num / 100
    dobro = num * 2
    print(f'O dobro de {num} é {dobro}.')
    metade = num / 2
    print(f'A metade de {num} é {metade}.')
    aumentar = 10 * num / 100
    print(f'{num} + 10% é {aumentar + num}')
    diminuir = 10 * num / 100
    print(f'{num} - 10% é {num - diminuir}')'''
