from time import sleep
times =('América', 'Athletico', 'Atlético', 'Bahia', 'Botafogo', 'Corintias',
        'Coritiba', 'Cruzeiro', 'Cuiabá', 'Flamengo', 'Fluminense', 'Fortaleza',
        'Goiás', 'Grémio', ' Internacional', 'palmeiras', 'Bragantino', ' Santos', 'são paulo',
        'Vasco da Gama')
sleep(0.8)
print('-=-=-=-=-=' * 15)
print(f'lista de times Brasileirão: {times}')
sleep(0.8)
print('-=-=-=-=-=' * 15)
print(f'os cinco primeiros são {times[0:5]}')
sleep(0.8)
print('-=-=-=-=-=' * 15)
print(f'os quatro utimos são{times[-4:]}')
sleep(0.8)
print(f'-=-=-=-=' * 15)
print(f'times em ordem alfabética: {sorted(times)}')
sleep(0.10)
print('-=-=-=-=' * 15)
print(f'o Fluminense está na {times.index("Fluminense")} posicão')
