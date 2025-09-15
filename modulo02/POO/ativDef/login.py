def acesso(usuario, senha):
    if usuario == "admin" and senha == "1234":
        return "Acesso concedido"
    else:
        return "Acesso negado"
usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")
print(acesso(usuario, senha))
    
    