class Livro:
    def __init__(self, titulos, autor):
        self.titulos  = titulos
        self.autor = autor
    
    
class Biblioteca:
    
    def __init__(self):
        self.acervo = []
        
    
    def adicionar_livro(self, livro):
        self.livro = Livro(titulos=livro.titulos, autor=livro.autor)
        self.acervo.append(self.livro)
        print(f"Livro '{livro.titulos}' adicionado com sucesso!")
        
        
    def lista_livros(self):
        if not self.acervo:
            print("A biblioteca está vazia.")
        else:
            print("Livros na biblioteca:")
            for livro in self.acervo:
                print(f"Título: {livro.titulos}, Autor: {livro.autor}")

livro1 = Livro("1984", "George Orwell")
livro2 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien")
biblioteca = Biblioteca()
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.lista_livros()


       
     
       
       
       
    