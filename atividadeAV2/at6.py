status = "inicio" 

print("--- Sistema de Atendimento ---")
print("Comandos: A (Abrir), T (Triagem), E (Encaminhar), F (Finalizar), S (Sair)")

while True:
    comando = input("\nDigite o comando: ").upper().strip()

    match comando:
        case "A" if status == "inicio":
            status = "aberto"
            print("Atendimento aberto com sucesso.")
        
        case "T" if status == "aberto":
            status = "triado"
            print("Triagem realizada.")
            
        case "E" if status == "triado":
            status = "encaminhado"
            print("Atendimento encaminhado para o especialista.")
            
        case "F" if status == "encaminhado":
            status = "inicio" 
            print("Atendimento finalizado com sucesso!")
            
        case "S":
            print("Saindo do sistema...")
            break
            
        case "A" | "T" | "E" | "F":
           
            print(f"Erro: Não é possível executar '{comando}' enquanto o status é '{status}'.")
            
        case _:
            print("Erro: Comando inválido.")