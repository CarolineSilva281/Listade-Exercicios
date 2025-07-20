#Definir uma senha correta no programa
senha_correta = "1234"
tentativas = 0
limite = 3

while tentativas < limite:
    #Pedir que o usuário digite uma senha.
    senha_digitada = input("Digite a senha: ")
#Comparar a senha digitada com a correta.
    if senha_digitada == senha_correta:
        #Mostrar mensagem de acesso permitido ou negado
        print("Acesso permitido.")
        break
    else:
        tentativas += 1
        print("Senha incorreta.")

        if tentativas < limite:
            print(f"Tentativas restantes: {limite - tentativas}")
        else:
            print("Número máximo de tentativas atingido. Acesso bloqueado.")