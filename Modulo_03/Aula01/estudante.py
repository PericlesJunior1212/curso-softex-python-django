from pessoa import Pessoa


class Estudante(Pessoa):

    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula
    
   
    def adicionar_nota(self, materia, nota):
        if materia not in self.notas:
            self.notas[materia] = []
        self.notas[materia].append(nota)
        
    

        
        
    