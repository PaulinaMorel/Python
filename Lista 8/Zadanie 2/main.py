import szyfrcezara
import open_save


word, program, key = open_save.open_file()

if program:    
    decoded_text = szyfrcezara.odszyfr(word,key)
    open_save.save_file(decoded_text,key)