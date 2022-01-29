from math import isclose
from itertools import combinations

class Klasa:
    def __init__(self, lista):
        self.lista = lista

    def potrojnePodlisty(self):
        if len(self.lista) < 3:
            return "Lista jest zbyt krotka"
        else:
            podlisty = []
            podlisty.extend([list(x) for x in combinations(self.lista, 3) if isclose(sum(x), 0, abs_tol=0.0)])
            return "lista nie spelnia warunku" if len(podlisty)==0 else podlisty

klasa = Klasa([1,-2,2,4,-3,2,-1])
print(klasa.potrojnePodlisty())