import math

class Ponto:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class SegmentoDeReta:
    
    def __init__(self, ponto1: Ponto, ponto2: Ponto):
            self.ponto1 = ponto1
            self.ponto2 = ponto2
            
    def calcular_comprimento(self):
        
        coord1 = (self.ponto1.x, self.ponto1.y)
        coord2 = (self.ponto2.x, self.ponto2.y)
        resultado = math.dist(coord1,coord2)
        return resultado

p1 = Ponto(2,3)
p2 = Ponto(5,7)
seg = SegmentoDeReta(p1,p2)
print(seg.calcular_comprimento())

