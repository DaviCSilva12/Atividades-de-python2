n = int(input("n: "))

if n < 0:
    print("Erro: n deve ser positivo.")
else:
    f = 1
    for k in range(1, n + 1):
        f *= k
        if f > 1_000_000:
            print(f"passou do limite em {k}!")
            print(f"valor acumulado: {f}")
            break
    else:
        print(f"O fatorial é {f}")