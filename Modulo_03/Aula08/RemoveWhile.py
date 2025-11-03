def remove(self, lista):
    self.lista = lista

    i = 0

    while i < len(self.lista):

        if 'a' in self.lista[i].lower():
            self.lista.pop(i)
        else:
            i += 1

    print("Lista após remoção:", self.lista)