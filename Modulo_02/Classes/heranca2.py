class Midia:
    def __init__(self, titulo, durac_seg):
        self.titulo = titulo
        self.durac_seg = durac_seg
    
    def exibir (self):
        print(f"O titúlo é {self.titulo} com {self.durac_seg} ")
        
class Musica(Midia):
    def __init__(self, titulo, durac_seg, artista):
           super().__init__(titulo, durac_seg)
           self.artista =  artista
    def exibir(self):
         print(f"O titúlo é {self.titulo}, com {self.durac_seg} minutos do artista {self.artista}.\n")

class Video(Midia):

    def __init__(self, titulo, durac_seg, resolucao):
         super().__init__(titulo, durac_seg)
         self.resolucao = resolucao
         
    def exibir(self):
         print(f"O titúlo é {self.titulo}, com {self.durac_seg} minutos e a resolução em {self.resolucao}.\n")
         
musicas1 = Musica("Jesus Chorou", 4, "Racionais")
videos1 = Video("Jesus Chorou", 4, "8K")

dicionarios_mida = {"musicas":[], "videos":[]}
dicionarios_mida["musicas"].append(musicas1)
dicionarios_mida["videos"].append(videos1)

print(dicionarios_mida)

for item in dicionarios_mida.values():
    for midia in item:
        midia.exibir()

    








    