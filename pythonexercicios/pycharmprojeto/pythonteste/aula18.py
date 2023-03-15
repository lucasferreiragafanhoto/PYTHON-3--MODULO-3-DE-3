num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
if 5 in num:
    num.remove(5)
else:
    print('não achei o número 5')
print(num)
print(f'ESSA LISTA TEM TANTOS{len(num)} ELEMENTOS.')