import pesel_generator
import save_pesel

rok, miesiac, dzien, cztery_cyfry, ostatnia_cyfra = pesel_generator.pesel() 
pesel_cyfry = rok + miesiac + dzien + cztery_cyfry + ostatnia_cyfra
print(pesel_cyfry)

pesel_do_zapisu = ""
number = 10
for i in range(number):
    rok, miesiac, dzien, cztery_cyfry, ostatnia_cyfra = pesel_generator.pesel() 
    pesel_cyfry = rok + miesiac + dzien + cztery_cyfry + ostatnia_cyfra
    pesel_do_zapisu = pesel_do_zapisu + pesel_cyfry + "\n"

save_pesel.save_file(pesel_do_zapisu)