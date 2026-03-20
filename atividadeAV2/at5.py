a = int(input("Início (a): "))
b = int(input("Fim (b): "))
p = int(input("Passo (p): "))

erro = False
if p == 0:
    erro = "Erro: O passo (p) não pode ser zero."
elif a < b and p <= 0:
    erro = "Erro: Para subir (a < b), o passo deve ser positivo."
elif a > b and p >= 0:
    erro = "Erro: Para descer (a > b), o passo deve ser negativo."

if erro:
    print(erro)
else:
    
    fim = b + (1 if p > 0 else -1)
    resultado = range(a, fim, p)
   
    for n in resultado:
        print(n, end=" ")
    
    print(f"\nTotal de valores impressos: {len(resultado)}")