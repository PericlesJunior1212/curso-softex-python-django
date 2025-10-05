from pessoa import Pessoa

class Estudante(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula
        self._notas = {}
    def adicionar_nota(self, materia, nota):
        if materia not in self._notas:
            self._notas[materia] = []
        self._notas[materia].append(nota)

    def mostrar_notas(self):
        print(self._notas)

    @property
    def notas(self):
        return self._notas
    
    



estd1 = Estudante(nome="Paulo", idade=25, matricula=2365)
estd1.adicionar_nota("Matemática", 9)
estd1.adicionar_nota("História", 8)
estd1.mostrar_notas()
