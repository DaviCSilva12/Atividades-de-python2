def eh_anagrama(texto1, texto2):
    
    limpar = lambda s: sorted(s.replace(" ", "").lower())
    
    return limpar(texto1) == limpar(texto2)

frase1 = input("Primeira palavra/frase: ")
frase2 = input("Segunda palavra/frase: ")

if eh_anagrama(frase1, frase2):
    print("É um anagrama!")
else:
    print("Não é um anagrama.")