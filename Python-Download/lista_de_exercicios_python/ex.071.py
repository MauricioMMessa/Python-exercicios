valor = int(input("Digite o valor a ser sacado: "))
cedulas_50 = valor // 50
valor = valor % 50
cedulas_20 = valor // 20
valor = valor % 20
cedulas_10 = valor // 10
valor = valor % 10
cedulas_1 = valor // 1
print(f"Serão entregues {cedulas_50} cédulas de R$50,00")
print(f"Serão entregues {cedulas_20} cédulas de R$20,00")
print(f"Serão entregues {cedulas_10} cédulas de R$10,00")
print(f"Serão entregues {cedulas_1} cédulas de R$1,00")
