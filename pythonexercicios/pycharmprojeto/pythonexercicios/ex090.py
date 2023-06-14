aluno = dict()
aluno['nome'] = str(input('NOME: '))
aluno['média'] = float(input(F'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'APROVADO'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'RECUPERAÇÃO'
else:
    aluno['situação'] = 'REPROVADO'
print('-= * 30')
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')
