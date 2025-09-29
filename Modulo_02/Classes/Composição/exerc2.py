class GraoDeCafe:
    def __init__(self):
        pass
        
    def moer(self):
        print("Os grãos de café foram moídos.")
        
        
class Agua:
    def __init__(self):
        pass 
    
    def aquecer(self):
        print("A água está aquecida.")

class Cafeteria:
    def __init__(self):
        self.grao = GraoDeCafe()
        self.agua = Agua()
        
    def prepar_cafe(self):
        self.grao.moer()
        self.agua.aquecer()
        print("O café está pronto.")
        
central_perk = Cafeteria()
central_perk.prepar_cafe()
