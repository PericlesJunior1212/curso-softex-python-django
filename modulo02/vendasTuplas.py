vendas = [("Teclado", 50,2),("Mouse", 25.50,4),("Monitor", 300, 1), ("Fone", 45, 1),("Webcam", 75.20, 2)]
produtos_unicos = set()
vendas_filtradas = []
for nome_produto, valor, qtd in vendas:
    mult = valor * qtd
    if mult >= 100:
        vendas_filtradas.append((nome_produto, valor, qtd))
    produtos_unicos.add(nome_produto)
     
    
print(f"\nAs vendas maiores que 100  sao: {vendas_filtradas}")    
print(f"\nSó os produtos, separados: {produtos_unicos}")
print("\n")

      