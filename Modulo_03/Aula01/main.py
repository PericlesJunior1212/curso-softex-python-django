from escola import Escola
from estudante import Estudante
escola = Escola()
estudante1 = Estudante("João", 20, 123455)
estudante2 = Estudante("Maria", 22, 67890)
escola.adicionar_estudante(estudante1)
escola.adicionar_estudante(estudante2)
escola.mostrar_relatorio()