import open_save
import pesel_check

pesels, pesels_number, program = open_save.open_file()
pesels_temp = []
pesels_to_save = ""

if program:    
    for i in range(pesels_number):
        state = pesel_check.check(pesels[i])
        if state:
            pesels_temp.append(pesels[i])
            year, month, day, gender = pesel_check.pesel_info(pesels_temp[i])
            pesels_to_save = pesels_to_save + "nr PESEL:\n%" + day + "%" + month + "%" + year + ";\t płeć: " + gender + "\n"
    
    open_save.save_file(pesels_to_save)