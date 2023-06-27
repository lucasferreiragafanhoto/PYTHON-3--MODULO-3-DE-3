from datetime import datetime
dados = dict()
dados ['nome'] = str(input('NOME:'))
nasc = int(input('ANO DE NACIMENTO:'))
dados ['idade'] = datetime.now().year - nasc
dados ['ctps'] =int(input('Carteira de trabalho (0 não tem):'))
if dados ['ctps'] != 0:
   dados ['contratação'] = int(input('ANO DE CONTRATAÇÃO: '))
   dados ['SALÁRIO'] = float(input('SALÁRIO: R$'))
   dados ['aposentadoria'] = dados ['idade'] +((dados ['contratação'] + 35 - datetime.now().year))
print('-=' * 30)
for k, v in dados.items():
    print(f' - {k} tem o valor {v} ')



