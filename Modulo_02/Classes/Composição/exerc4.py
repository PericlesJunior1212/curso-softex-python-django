class Teclado:
    def __init__(self):
        pass
    def ligar(self):   
        print("O teclado está ligando.....")

class Mouse:
    def __init__(self):
         pass
         
    def ligar(self):
        print("O mouse está ligando.....")
    
class Monitor:
    def __init__(self):
        pass
    
    def ligar(self):
        print("O monitor está ligando....")

class Computador:
    def __init__(self):
        self.tecl = Teclado()
        self.Mous = Mouse()
        self.mon = Monitor()
    def ligar_computador(self):
        
        self.tecl.ligar()
        self.Mous.ligar()
        self.mon.ligar()
        print("O computador está pronto para uso.")
        
ligando = Computador()
ligando.ligar_computador()