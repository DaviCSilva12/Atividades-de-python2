def eh_palindromo(texto):
    texto = texto.lower()
    
    texto_limpo = ""
    for c in texto:
        if c.isalnum():
            texto_limpo += c
    
    return texto_limpo == texto_limpo[::-1]


entrada = input("Digite: ")

if eh_palindromo(entrada):
    print("É palíndromo")
else:
    print("Não é palíndromo")