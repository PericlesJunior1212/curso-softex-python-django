class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome  
        self._idade = idade
        
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome_novo: str):
        if not isinstance(nome_novo, str):
            print("Nome deve ser do tipo string")
        elif not nome_novo:
            print("Nome não pode ser vazio")
        else:
            self._nome = nome_novo

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, nova_idade: int):
        
        if isinstance(nova_idade, int) and  nova_idade  > 0:
            self._idade = nova_idade
        else:
            print("Idade deve ser um número inteiro positivo")
              
p1 = Pessoa("João", 30)
print(f"Nome: {p1.nome}, Idade: {p1.idade}")
p1.nome = "Maria"
p1.idade = 25
print(f"Nome: {p1.nome}, Idade: {p1.idade}")
p1.nome = ""
p1.idade = -5
print(f"Nome: {p1.nome}, Idade: {p1.idade}")

            
           
            


    