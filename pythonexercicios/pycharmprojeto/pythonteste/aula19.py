valores = list()
valores.append(5)
valores.append(9)
valores.append(4)
valores.append(3)
for c, v in enumerate(valores):
    print(f'posição {c} encontrei o valores {v}!')
print('cheguei ao final da lista.')


#segunda maneira de lista

valores = list()
for cont in range(0, 5):
    valores.append(int(input('digite um valor:')))
for c, v in enumerate(valores):
    print(f'na posição {c} encontrei o valor {v}!')
print('cheguei ao final da lista.')
