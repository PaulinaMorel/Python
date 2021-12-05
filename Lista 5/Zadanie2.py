def zamiana(liczba):
    jedn = ("", "jeden ", "dwa ", "trzy ", "cztery ","pięć ", "sześć ", "siedem ","osiem ", "dziewięć ", "dziesięć ", "jedenaście ", "dwanaście ", "trzynaście ", "czternaście ", "piętnaście ","szesnaście ", "siedemnaście ", "osiemnaście ", "dziewiętnaście")
    dzies =("", "", "dwadzieścia ", "trzydzieści ", "czterdzieści ", "pięćdziesiąt ","sześćdziesiąt ","siedemdziesiąt ","osiemdziesiąt ","dziewięćdziesiąt ")

    if liczba<20:
        return  jedn[liczba] #jak mniejsza od 20 to bierze wartosc z tabeli pierwsze pole jest puste zeby sie nie psulo
    if liczba<100:
        return  dzies[liczba // 10]  +jedn(int(liczba % 10)) #dzieli przez 10 zeby tez uzyskac wart. z tabeli i dodaje reszte z podzielenia tej liczby na 10 
        # w sensie jak jest 27 to dwadziescia na 10 daje dwa-wart. dwadziescia, a modulo  z 27 i 10 to 7 czyli wartosc 7 z tabeli-siedem
    if liczba<1000:
        return jedn[liczba // 100]  +"set " +zamiana(int(liczba % 100)) #analogicznie robi to samo czyli liczbe na 100 zeby dostac wartosc z PIERWSZEJ tabeli dodaje slownie sto
        #potem leci od nowa funkcje juz dla 2cyfrowej liczby np 135 dzieli liczbe na 100 bez reszty(?) w sensie zostaje 1 czyli wart. pierwsza z tabeli
        #zeby zostalo 35 bierze rezte z dzielenia przez 100 czyli to 35 i cisnie od poczatku czyli sprawdza czy mniejsze od 20-nie, od 100-tak
        #czyli to samo co napisalam wyzej
    if liczba<2000: 
        return  zamiana(liczba // 1000) + "tysiąc " + zamiana(int(liczba % 1000))
        #i znowu robi funckje z pelnych liczb z dzielenia przez 1000 zeby dostac liczbe <20 czyli zlapac sie pod pierwszego ifa, dodaje slownie tysiac, i leci z funkcja 
        #dla liczby jakiejstam 3 cyfrowej np 1654- najpierw ogarnia ile jest tysiecy a potem robi funkcje dla 654, czyli dzieli setki zeby bylo 6set i tak dalej...


liczba = int(input("podaj liczbe z zakresu 1-1999: "))
print(zamiana(liczba))