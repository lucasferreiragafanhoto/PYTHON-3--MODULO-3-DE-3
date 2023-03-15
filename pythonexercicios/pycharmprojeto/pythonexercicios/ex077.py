from time import sleep
palavras = ('aprendre', 'progamar', 'linguagem', 'python', 'cursos', 'gratis',
            'estudar', 'mercado', 'progamador')
for p in palavras:
    sleep(0.8)
    print(f'\n\033[1:30:44mNa  palavra -> {p.upper()} temos->', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end='')


