from time import sleep
listanum = []
mai = 0
mem = 0
for c in range(0, 5):
    sleep(0.2)
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    sleep(0.5)
    listanum.sort()
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            mem = listanum[c]
print('=-'* 30)
print(f'voçê digitou os valores{listanum}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f' {i}... ', end='')
print()
print(f'O menor valor digitado foi {mem} nas posicões', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f' {i}... ', end='')
print()


















