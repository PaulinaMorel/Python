import os

def save_file(pesel):
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
        file_save = open(path + "\PESEL.txt", "w")
        file_save.write(pesel)
        file_save.close()