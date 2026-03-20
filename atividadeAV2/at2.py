hora = int(input("Hora (0-23): "))
chuva = int(input("Chuva (0 ou 1): "))
fluxo = int(input("Fluxo (0-Baixo, 1-Médio, 2-Alto): "))

tempo = 60 if (7 <= hora <= 9) or (17 <= hora <= 19) else 35

if chuva:
    tempo *= 1.2

ajustes_fluxo = {0: -10, 1: 0, 2: 15}
tempo += ajustes_fluxo.get(fluxo, 0)

print(f"Tempo final do semáforo: {tempo:.1f}s")