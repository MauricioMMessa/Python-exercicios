aluno = dict()
aluno['nome'] = str(input('Nome: ')).strip() .title()
aluno['nota'] = float(input('Nota: '))
if aluno['nota'] <= 59:
    aluno['situação'] = 'REPROVADO'
elif aluno['nota'] >= 60 and aluno['nota'] <= 69:
    aluno['situação'] = 'RECUPERAÇÃO'
else:
    aluno['situação'] = 'APROVADO'
print('-=' * 20)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
