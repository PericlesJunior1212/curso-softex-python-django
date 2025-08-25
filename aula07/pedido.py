hamb = 30.00
cupom_desc=  "10"

while True:
    produto = input("Me diga seu pedido: ")
    
    if produto == "hamburguer":
        print(f"O valor do seu pedido é R$ {hamb}")
        break
    else:
        print("Produto indisponível")
        
cupom = input("Você possui cupom de desconto? (s/n) ")
if cupom == "s":
        print(f"Valor com desconto: R$ {hamb *0.9}")
else:
        print(f"Valor sem desconto: R$ {hamb}")
print("Volte sempre!")
     