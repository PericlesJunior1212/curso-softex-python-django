produtos = {"camiseta": 20.00, "calça": 35.00, "tênis": 50.00}
remove = input("Digite o nome do produto que deseja remover: ")
if remove in produtos:
    del produtos[remove]
    print(f"Produto {remove} removido com sucesso!")
nova_lista = produtos.items()
print(nova_lista)
    
