class funcionario:
    def __init__(self, nome, salario, perc_bon = 10 ):
        self.nome = nome
        self.salario = salario
        self.perc_bon = perc_bon
    def calcular_bonus(self):
        novo_salario = self.salario + (self.salario * self.perc_bon/100)
        self.salario = novo_salario
func1 = funcionario("Péricles", 2000)
func2 = funcionario("Ana", 3000, 15)
func1.calcular_bonus()
func2.calcular_bonus()
print(f"Nome: {func1.nome}, Salário com bônus: {func1.salario}")
print(f"Nome: {func2.nome}, Salário com bônus: {func2.salario}")


        
        

   