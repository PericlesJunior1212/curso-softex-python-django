produtos = {"camiseta": 20.00, "calça": 35.00, "tênis": 50.00, "jaqueta": 80.00, "boné": 15.00}

produto_mais_caro = max(produtos, key=produtos.get)
valor_mais_caro = produtos[produto_mais_caro]

print(f"O produto mais caro é '{produto_mais_caro}' custando R$ {valor_mais_caro:.2f}")









