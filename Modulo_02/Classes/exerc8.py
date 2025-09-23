class Carro:
    def __init__(self, modelo, nivel_combustivel=0):
        self.modelo = modelo
        self.nivel_combustivel = nivel_combustivel  # em litros
    
    def abastecer(self, litros):
        self.nivel_combustivel += litros
        print(f"Abastecido com {litros} litros. Nível atual: {self.nivel_combustivel} litros")
    
    def dirigir(self, distancia):
        consumo = distancia / 10  # 1 litro a cada 10 km
        
        if consumo > self.nivel_combustivel:
            print("Combustível insuficiente para a distância desejada.")
            distancia_possivel = self.nivel_combustivel * 10
            self.nivel_combustivel = 0
            print(f"O carro percorreu {distancia_possivel} km e ficou sem combustível.")
        else:
            self.nivel_combustivel -= consumo
            print(f"O carro percorreu {distancia} km. Combustível restante: {self.nivel_combustivel} litros")


meu_carro = Carro("Fusca")
meu_carro.abastecer(50)  
meu_carro.dirigir(200)   
meu_carro.dirigir(400)   