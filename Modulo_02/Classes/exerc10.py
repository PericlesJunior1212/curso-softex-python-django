class Motor:
    def __init__(self, potencia):
        self.potencia = potencia  
class Carro:
    def __init__(self, modelo, motor: Motor):
        self.modelo = modelo
        self.motor = motor(100)
    def exibir_potencia(self):
        return self.motor.potencia
meu_carro = Carro("Fusca", Motor)
print(f"O motor do {meu_carro.modelo} tem {meu_carro.exibir_potencia()} cavalos de potência.")
        
