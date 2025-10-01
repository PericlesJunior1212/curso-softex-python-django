from pessoa import Pessoa


class Estudante(Pessoa):

    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula
        self._notas = {}
   
    def adicionar_nota(self, materia, nota):
        if materia not in self.notas:
            self.notas[materia] = []
        self.notas[materia].append(nota)

    
    def mostrar_notas(self):
        print(f"{self._notas}")
        
    
        @property
        def notas(self):
         return self._notas
    
        @notas.setter
        def notas(self, materia, notas):
        
         if materia not in self.notas:
            self._notas[materia] = []
         self._notas[materia].append[notas]
         
estd1 = Estudante(nome="paulo", idade=25, matricula=2365)
print(Estudante.mostrar_notas(estd1))

        
        
        
    
    
        
    

        
        
    