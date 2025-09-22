estoque= {"camiseta": 50, "calça": 20, "tênis": 15, "jaqueta": 10, "boné": 30}
vendas = {"camiseta": 5, "calça": 2, "tênis": 1, "jaqueta": 0, "boné": 3}
total_vendas = 0
for produto, quantidade in vendas.items():
    if produto in estoque:
        if quantidade <= estoque[produto]:
            total_vendas += quantidade
            estoque[produto] -= quantidade
        else:
            print(f"Estoque insuficiente para {produto}.")
    else:
        print(f"Produto {produto} não encontrado no estoque.")
print("Total de itens vendidos:", total_vendas)
print("Estoque atualizado:", estoque)
