class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
produto1 = Produto("Camisa", 50.0)
produto2 = Produto("Calça", 100.0)
produto3 = Produto("Tênis", 150.0)
print(f"O produto {produto1.nome} custa R$ {produto1.preco:.2f}.")
print(f"O produto {produto2.nome} custa R$ {produto2.preco:.2f}.")
print(f"O produto {produto3.nome} custa R$ {produto3.preco:.2f}.")

