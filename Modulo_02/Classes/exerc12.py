class Filme:
    def __init__(self, titulo, diretor, ano):
        self.titulo = titulo
        self.diretor = diretor
        self.ano = ano

    def __str__(self):
        return f"Filme: '{self.titulo}' Ano: {self.ano} - Diretor: {self.diretor}"




filme = Filme("A volta dos que não foram.", "Sayn Bagla", 1290)
print(filme)