class Musicas:
    def __init__(self, titulo, artista):
        self.titulo = titulo
        self.artista = artista

class Playlist:
    def __init__(self, list_mus:list[Musicas]):
        
        self.lista_musica = list_mus
        
        
    def adcion_mus(self):
        