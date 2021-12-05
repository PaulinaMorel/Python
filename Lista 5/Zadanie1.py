slownik={ "zero": 0,"jeden": 1, "dwa":2,"trzy" :3, "cztery": 4, "pięć": 5, "sześć": 6, "siedem" : 7, "osiem" : 8, "dziewięć":9, "dziesięć": 10, "jedenaście": 11,
         "dwanaście": 12, "trzynaście": 13, "czternaście":14, "piętnaście": 15, "szesnaście":16, "siedemnaście":17, "osiemnaście":18, "dziewiętnaście":19,
         "dwadzieścia":20, "trzydzieści":30, "czterdzieści":40, "pięćdziesiąt":50}

def zamiana(m,n):
    d=0
    j=0
    if(m in slownik): #sprawdza czy pierwszy element pasuje do slownika jak tak to bierze jego wartość
        d=(slownik.get(m))
    if(n in slownik):
        j=(slownik.get(n)) #analogicznie z drugim
    print(d+j) #dodaje do siebie te dwa i daje wynik


x= input("Podaj słownie liczbę: ")
y=x.split() #rozdziela slowa na tablice(?) no w sensie jak jest dwadzieścia dwa to osobno bierze dwadziescia i osobno dwa
zamiana(y[0],y[1]) #i do funkcji leci 1 i drugi element tabeli