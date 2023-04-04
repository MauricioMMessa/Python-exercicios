produto = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20,'Compasso', 9.99,
           'Mochila', 120.32, 'Caneta', 22.30, 'Livro', 34.90)
print('~' * 50)
print('Lista de preços'.center(50))
print('~' * 50)
for p in range(0, len(produto), 2):
    print(f'{produto[p]:.<30}R$ {produto[p+1]:>.2f}')
print('_' * 50)
