palavras = input("Digite as palavras separadas por espaço: ").split()
termo_busca = input("Qual palavra deseja encontrar? ")

encontrado = False

for indice, palavra in enumerate(palavras):
    if palavra.lower() == termo_busca.lower():  
        print(f"Palavra encontrada no índice: {indice}")
        encontrado = True
        break  
if not encontrado:
    print("A palavra não foi encontrada na lista.")