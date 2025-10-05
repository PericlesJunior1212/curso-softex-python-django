from estudante import Estudante

class Escola:
    
    def __init__(self): 
        self.lista_estudante = []
        
    def adicionar_estudante(self, estudante: Estudante):
        self.lista_estudante.append(estudante)
    
    def mostrar_relatorio(self):
        for estudante in self.lista_estudante:
            print(f"Nome: {estudante.nome}, Idade: {estudante.idade}, Matrícula: {estudante.matricula}")
            estudante.mostrar_notas()
            print("-----")
        