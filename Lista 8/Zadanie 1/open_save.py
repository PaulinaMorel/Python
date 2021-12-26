import os
import datetime

def open_file():
    path = input("podaj sciezke pliku txt: ")
    if not os.path.exists(path):
        print("nie istnieje")
        word = ""
        program = False
        return word,program
    else:
        print("Plik istnieje")
        program = True
        file_open = open(path, "r")
        word = file_open.read()
        file_open.close()
        return word,program


def save_file(coded_text,key):
    path = input("podaj sciezke zapisu pliku txt: ")
    if not os.path.exists(path):
        print("folder nie istnieje")
        print("zaraz zostanie stworzony")
        try:
            os.mkdir(path)
        except OSError:
            print("nie udalo sie stworzyc folderu")
        else:
            print("stworzono folder")

    if os.path.exists(path):
        date = datetime.datetime.now()
        key_str = str(key)
        Y = str('{:02d}'.format(date.year))
        m = str('{:02d}'.format(date.month))
        d = str('{:02d}'.format(date.day))
        file_save = open(path + "\plik_zaszyfrowany%" + key_str + "_%" + Y + "%" + m + "%" + d + ".txt", "w")
        file_save.write(coded_text)
        file_save.close()