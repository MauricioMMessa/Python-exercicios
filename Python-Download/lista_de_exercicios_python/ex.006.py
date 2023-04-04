n = int(input('Digite um número: '))
cores = {'limpa':'\033[m', 'verde':'\033[32m'}
print('O dobro do número escolhido é: {}{}{}!\nO triplo: {}{}{}!\nE a raiz quadrada: {}{:.2f}{}!'
      .format(cores['verde'], n*2, cores['limpa'], cores['verde'], n*3, cores['limpa'], cores['verde'], n**(1/2), cores['limpa']))
