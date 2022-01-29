import xml.etree.ElementTree as ET

class PrzeliczanieWalut:
    def __init__(self, path):
        self.path = path
        self.tree = ET.parse(path)
        self.root = self.tree.getroot()

    def wypiszListe(self): 
        for elem in self.root:
            for subelem in elem:
                print(subelem.text)

    def PLN(self, wal, pln):
        for nazwa_waluty, przelicznik, kod_waluty, kurs_sredni in self.root.iter('pozycja'):
            if wal == kod_waluty.text:
                return f"{pln * float(przelicznik.text) / float(kurs_sredni.text)} {kod_waluty.text}"

    def toPLN(self, wal, ile):
        for nazwa_waluty, przelicznik, kod_waluty, kurs_sredni in self.root.iter('pozycja'):
            if wal == kod_waluty.text:
                return f"{ile * float(przelicznik.text) * float(kurs_sredni.text)} {'PLN'}"

    def walToWal(self,wal,wal2,ile):
       for nazwa_waluty, przelicznik, kod_waluty, kurs_sredni in self.root.iter('pozycja'):
          if wal == kod_waluty.text:
            temp =ile * float(przelicznik.text) * float(kurs_sredni.text)

       for nazwa_waluty, przelicznik, kod_waluty, kurs_sredni in self.root.iter('pozycja'):
          if wal2 == kod_waluty.text:
             return f"{temp * float(przelicznik.text) / float(kurs_sredni.text)} {kod_waluty.text}"

x = int(input(
    "Wybierz opcje \n1 - lista kursow, \n2 - zamiana PLN na wybrana walute, \n3 - zamiana wybranej waluty na PLN, \n4 - konwersja wybranej waluty na inna wybrana walute "))
if x == 1:
    przel = PrzeliczanieWalut('waluty.xml')
    print(przel.wypiszListe())
elif x == 2:
    wal = input("Podaj kod wybranej waluty:")
    pln = float(input("Podaj ile PLN chcesz zamienic:"))
    przel = PrzeliczanieWalut('waluty.xml')
    print(przel.PLN(wal, pln))
elif x == 3:
    wal = input("Podaj kod wybranej waluty:")
    ile = float(input("Podaj ile chcesz zamienic:"))
    przel = PrzeliczanieWalut('waluty.xml')
    print(przel.toPLN(wal, ile))
elif x== 4:
   wal = input("Podaj kod waluty, którą chcesz zamienić:")
   wal2 = input("Podaj kod waluty, którą chcesz otrzymać:")
   ile = float(input("Podaj ile chcesz zamienic:"))
   przel = PrzeliczanieWalut('waluty.xml')
   print(przel.walToWal(wal,wal2,ile))