from time import sleep
cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
        'seis', ' sete', 'oito', 'nove', 'dez', 'onze',
        'doze', 'treze', ' catorze', 'quinze', 'dezesseis',
        'dezessete', 'dezoito', 'dezenove', 'vinte',)
while True:
    núm = int(input('digite um número entre 0 e 20: '))
    if 0 <= núm <= 20:
        break
    print('tente novamente. ', end='')
print(f'voçê digitou o número {cont[núm]}')
sleep(0.5)
opcao = str(input('quer continuar a ler os números  por extenso? [S/N]')).upper().strip()
while opcao == 'S':
    sleep(0.8)
    núm = int(input('entao digite outro número:'))
    print(f'voçê digitou o número {cont[núm]}')
    sleep(0.8)
    opcao = str(input('quer continuar a ler os números por extenso? [S/N]')).upper().strip()
while opcao == 'N':
    sleep(0.14)
    exit('OBRIGADO VOLTE SEMPRE.')














