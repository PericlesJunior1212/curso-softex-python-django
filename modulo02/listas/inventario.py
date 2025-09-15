estoque_fisico = [("Camiseta", 101),("Calça", 102), ("Boné", 103), ("Tênis", 104)]
estoque_online = [("Boné", 103), ("Camisa Polo", 105), ("Calça", 102), ("Chinelo", 106)]
fisica = set(estoque_fisico)
online = set(estoque_online)
intersecao = fisica.intersection(online)
diferenca = fisica.difference(online)
diferenca_inver = online.difference(fisica)





print(f"\nProduto disponivéis na loja física e online: {intersecao}")
print(f"\nDisponiveis em loja física: {diferenca}")
print(f"\nDisponiveis em loja online: {diferenca_inver}")