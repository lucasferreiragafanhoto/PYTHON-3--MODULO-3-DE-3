from random import randint
from time import sleep
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('os valores sortes foram:', end='')
sleep(0.8)
for n in numeros:
    print(f'{n}', end='')
    sleep(0.8)
print(f'\n o maior valor sorteado foi {max(numeros)}')
sleep(0.8)
print(f' o menor valor sorteado foi {min(numeros)}')




