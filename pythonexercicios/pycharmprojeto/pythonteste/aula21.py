teste= list ()
teste.append('gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

pessoas = ['joã', 19],  ['Ana', 33],  ['Maria', 45]
print(pessoas[0])
print(pessoas[1])
print(pessoas[2])


pessoas = [['joão', 19],  ['Ana', 33], ['joaquim', 13],  ['Maria', 45]]
for g in pessoas:
    print(f'{g[0]} tem {g[1]} anos de idade. ')


galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome:')))
    dado.append(int(input('Idade:')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idadede.')
        totmen += 1
    print(f'temos {totmai} maor e {totmen} menor de idadede.')





