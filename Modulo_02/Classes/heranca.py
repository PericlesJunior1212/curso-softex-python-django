class Pessoa:
    def __init__(self, nome, idade):
        
        self.nome = nome
        self.idade =  idade
    def apresentar(self):
        print(f"Nome:{self.nome} Idade: {self.idade}")
    
class Estudante(Pessoa):
        def __init__(self, nome, idade, curso):
            super().__init__(nome, idade)
            self.curso = curso
        def apresentar(self):
          print(f"Nome:{self.nome} Idade: {self.idade} Curso: {self.curso}")
        
        
p1 = Pessoa("Carlos", 27)
estd = Estudante("Carlos", 27, "Softex")

lista = [p1, estd]

for puxar in lista:
    puxar.apresentar()

    