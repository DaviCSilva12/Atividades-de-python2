n = int(input("n: "))

if n <= 0:
    print("Erro: n deve ser maior que 0.")
else:
    soma = 0
    
    for i in range(1, n):
        if n % i == 0:
            soma += i  
    if soma == n:
        tipo = "perfeito"
    elif soma > n:
        tipo = "abundante"
    else:
        tipo = "deficiente"

    print(f"Soma: {soma}")
    print(f"Classificação: {tipo}")