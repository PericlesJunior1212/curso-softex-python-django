import math
class Circulo:
    
    def __init__(self, raio):
        self.__raio = raio

    @property
    def raio(self):
        return self.__raio
    @raio.setter
    def raio(self, novo_raio):
        if isinstance(novo_raio, (int, float)) and novo_raio > 0:
            self.__raio = novo_raio
        else:
            print("Raio deve ser um número positivo")
    def calcular_raio(self):
        return math.pi *(self.raio **2)
c1=Circulo(5)
area=c1.calcular_raio()
print(f"A área do círculo é: {area:.2f}")


        
        


    
    
    



       
    
        