import math

class Kolo:
    def __init__(self,promien):
        self.promien = promien

    def pole(self):
        return math.pi * self.promien ** 2

    def obwod(self):
        return 2 * math.pi * self.promien

r = int(input())
klasa = Kolo(r)
print(klasa.pole())
print(klasa.obwod())