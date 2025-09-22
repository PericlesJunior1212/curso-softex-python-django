class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


pessoa1 = Pessoa("João", 25)
pessoa2 = Pessoa("Maria", 30)
pessoa3 = Pessoa("Pedro", 17)
print(f"Olá, {pessoa1.nome}. Você tem {pessoa1.idade} anos.")
print(f"Olá, {pessoa2.nome}. Você tem {pessoa2.idade} anos.")
print(f"Olá, {pessoa3.nome}. Você tem {pessoa3.idade} anos.")
