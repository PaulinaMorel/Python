import szyfrcezara
import open_save


word, program = open_save.open_file()

if program:    
    condition = True
    while condition:
        key = int(input("Podaj klucz od 1-10: "))
        if 1 <= key <= 10:
            condition = False

    coded_text = szyfrcezara.szyfr(word,key)

    open_save.save_file(coded_text,key)