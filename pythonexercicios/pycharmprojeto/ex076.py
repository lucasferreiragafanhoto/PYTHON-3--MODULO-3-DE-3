from time import sleep
listagem = ('LÁPIS', 1.75,
            'BORRACHA', 2.00,
            'CADERNO', 15.00,
            'COLA', 4.50,
            'COMPASSO', 8.00)
sleep(0.8)
print('-' * 40)
print(f'\033[1:34:40m{"LISTAGEM DE PREÇOS":^40}')
sleep(0.8)
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        sleep(0.8)
        print(f'{listagem[pos]:.<30}', end=' ')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-'*40)
sleep(0.10)
exit('OBRIGADO POR ADQUIRIR NOSSOS PRODUTOS! VOLTE SEMPRE')





















