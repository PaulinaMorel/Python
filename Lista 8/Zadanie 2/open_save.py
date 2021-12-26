import os
import datetime

def open_file():
    print("dane pliku")
    path = input("podaj sciezke folderu w ktorym znajduje sie plik txt: ")
    if not os.path.exists(path):
        print("folder nie istnieje")
        word = ""
        key = ""
        program = False
        return word,program
    else:
        print("folder istnieje")
        key = int(input("podaj klucz: "))
        key_file = str(key)
        Y = str(input("rok: "))
        m = str(input("miesiac: "))
        d = str(input("dzien: "))
        path = path + "\plik_zaszyfrowany%" + key_file + "_%" + Y + "%" + m + "%" + d + ".txt"
        if not os.path.exists(path):
            print("plik nie istnieje")
            word = ""
            program = False
            return word,program,key
        else:
            program = True
            file_open = open(path, "r")
            word = file_open.read()
            file_open.close()
            return word,program,key


def save_file(decoded_text,key):
    path = input("podaj sciezke zapisu pliku txt: ")
    if not os.path.exists(path):
        print("folder nie istnieje")
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
        file_save = open(path + "\plik_odszyfrowany%" + key_str + "%" + Y + "%" + m + "%" + d + ".txt", "w")
        file_save.write(decoded_text)
        file_save.close()