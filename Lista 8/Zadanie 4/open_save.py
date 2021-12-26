import os

def open_file():
    path = input("podaj sciezke folderu w ktorym znajduje sie plik txt: ")
    if not os.path.exists(path):
        print("folder nie istnieje")
        pesels = []
        pesels_number = 0
        program = False
        return pesels, pesels_number, program
    else:
        print("folder istnieje")
        path = path + "\PESEL.txt"
        if not os.path.exists(path):
            print("plik nie istnieje")
            pesels = []
            pesels_number = 0
            program = False
            return pesels, pesels_number, program
        else:
            pesels = []
            number = [""] * 11
            file_open = open(path, "r")
            input_data = file_open.readlines()
            pesels_number = len(input_data) 
            for i in range(len(input_data)):
                pesels.append(input_data[i][:11])

            file_open.close()
            program = True
            return pesels, pesels_number, program

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
        file_save = open(path + "\PESEL_info.txt", "w")
        file_save.write(pesel)
        file_save.close()