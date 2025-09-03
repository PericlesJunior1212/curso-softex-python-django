acessos = [("Pedro", "sucesso"), ("Ana","falha"), ("Maria","sucesso"),("Pedro","falha"),("Ana","falha")]
usuario_sucesso = set()
usuario_falha = set()

for usuario, status_login in acessos:
  if status_login == "sucesso" :
      usuario_sucesso.add(usuario)
  elif status_login == "falha":
      usuario_falha.add(usuario)
  somen_falha = usuario_falha.difference(usuario_sucesso)

print(F"Os usúarios teve pelo menos um login bem-sucedidos foram: {usuario_sucesso}") 

print(f"Esses nao teve o login bem sucedido: {somen_falha}")
  
     