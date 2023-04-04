from ex112.utilidadesCeV import moeda
from ex112.utilidadesCeV import dado

p = dado.LeiaDinheiro('Digite o preço: R$')
print(moeda.resumo(p, 25, 10))
