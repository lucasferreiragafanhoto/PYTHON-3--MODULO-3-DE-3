from time import sleep
núm = (int(input('digite um número: ')),
       int(input('digite outro número:')),
       int(input('digite mais um número:')),
       int(input('digite o útimo número:')))

print(f'voçê digitou os valores {núm}')

print(f' o valor 9 apareceu {núm.count(9)} vezes')
if 3 in núm:
       print(f' o valor 3 apareceu na {núm.index(3)+1} posição')
else:
       print(' os valor pares digitados foram ', end='')
for n in núm:
    if n % 2 == 0:
        print(n, end=' ')