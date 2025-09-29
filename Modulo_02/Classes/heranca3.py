class FormaGeom:
    def __init__(self, cor):
        self.cor = cor
    def calcul_area(self):
        pass
     
class Retangulo(FormaGeom):
    def __init__(self, cor, largura, altura):
        super().__init__(cor)
        self.largura = largura
        self.altura = altura
    def calcul_area(self):
        
        
        return self.largura * self.altura
    
     
class Quadrado(Retangulo):
    def __init__(self, cor, lado):
        super().__init__(cor, lado, lado)
        
    @property
    def lado(self):
        return self.largura
    @lado.setter
    def lado(self, valor):
        self.largura = valor
        self.altura = valor
    
    
        
    def calcul_soma_areas(Formas):
        soma = 0
        for item in Formas:
            soma += item.calcul_area()
            print(f"A área {item.cor} tem a soma total: {soma}")

        return

ret = Retangulo("vermelho", 4, 5)
quad = Quadrado("azul", 4)
formas = [ret, quad]
print(Quadrado.lado)
print(Quadrado.calcul_soma_areas(formas))
print(Retangulo.calcul_area(ret))
print(Quadrado.calcul_area(quad))
 