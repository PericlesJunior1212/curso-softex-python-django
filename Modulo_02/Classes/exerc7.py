class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def calcular_area(self):
    
        
        return self.base * self.altura
    
    def calcular_perimetro(self):
        
        
        return 2 * (self.base + self.altura)
    
retang_1 = Retangulo(10,25)
area = retang_1.calcular_area()
print(f"O calculo da aréa: {area}")
perimt = Retangulo(10,25)
perimetro = perimt.calcular_perimetro()
print(f"O calculo do perimetro: {perimetro}")