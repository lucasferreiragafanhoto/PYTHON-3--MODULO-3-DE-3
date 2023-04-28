números = list()
while True:
    n = int(input('Digite um valor:'))
    if n not in números:
        números.append(n)
        print('valores adicionados com sucesso...')
    else:
        print('valores duplicado! Não vou adicionar...')
    r = str(input('quer continuar? [S/N]' ))
    if r in 'Nn':
        break
print('-= * 30')
números.sort()
print(f'voçê digitou os valores {números}')