class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


pessoa1 = Pessoa("João", 25)
pessoa2 = Pessoa("Maria", 30)
pessoa3 = Pessoa("Pedro", 17)
print(pessoa1.nome, pessoa1.idade)
print(pessoa2.nome, pessoa2.idade)
print(pessoa3.nome, pessoa3.idade)