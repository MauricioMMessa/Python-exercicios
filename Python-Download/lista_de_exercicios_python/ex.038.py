num1 = int(input('\033[4;32mValor 1:\033[m  Digite um número: '))
num2 = int(input('\033[4;31mValor 2:\033[m Digite um número: '))
if num1 > num2:
    print('\033[1;32mO primeiro valor é maior!\033[m')
elif num2 > num1:
    print('\033[1;32mO segundo valor é maior!\033[m')
elif num1 == num2:
    print('\033[1;32mNão existe valor maior, os dois são iguais!\033[m')
