times = ('PALMEIRAS', 'INTERNACIONAL', 'FLUMINENSE', 'CORINTHIANS', 'FLAMENGO', 'ATHLETICO-PR', 'ATLÉTICO-MG', 'FORTALEZA', 'SÃO PAULO',
'AMÉRICA-MG', 'BOTAFOGO', 'SANTOS', 'GOIÁS', 'RED BULL BRAGANTINO', 'CORITIBA', 'CUIABÁ', 'CEARÁ', 'ATLÉTICO-GO', 'AVAÍ', 'JUVENTUDE')
print(f'Os 5 primeiros times de 2022 é: ' ,end='')
for time in range(0, 5):
    print(f'{times[time]}', end=', ')
print(f'\nOs ultimos 4 colocados são: ', end='')
for time2 in range(16, 21 -1):
    print(f'{times[time2]}', end=', ')
print('\nOs times em ordem alfabética são: ',sorted(times))
print(f'O time do Corinthias ta na {times.index("CORINTHIANS")+1}º posição!')
