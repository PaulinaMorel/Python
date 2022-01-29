from itertools import combinations

class Klasa:
    def __init__(self, lista):
        self.lista = lista

    def podlisty(self):
        podlisty = []
        for x in range(0,len(self.lista)+1):
            podlisty.extend([list(i) for i in combinations(self.lista,x)])
        return podlisty


klasa = Klasa([1,2,3])
print(klasa.podlisty())
