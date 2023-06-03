pessoas = { 'nome': 'Gustavo', ' sexo': 'M', 'idade': 22}
print(f' o {pessoas ["nome"]} tem { pessoas["idade"]} anos. ')
print('-=' * 30)

pessoas = {'nome': 'gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas.values())
print('-=' * 30)


pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas.items())
print('-=' * 30)


pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
for k in pessoas.keys():
    print(k)
print('-=' * 30)


pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('-=' * 30)

" nesta tupla abaixo  mostra como adicionar outro nome "

pesoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
pessoas ['nome'] = 'leandro'
for k, v in pessoas.items():
    print(f' {k} = {v}')
print('-=' * 30)

" esta tupla mostra como adicionar peso "

pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
pessoas['peso'] = 98.5
for k, v in pessoas.items():
    print(f' {k} = {v} ')
print('-=' * 30)

" agora vamos mostrar como coocar um dicionario dentro de uma lista "

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end='')
    print()



