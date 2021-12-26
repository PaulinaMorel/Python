import random

def pesel():

    year = random.randint(1800, 2299)

    #+20, 40, 60, 80 aby odroznic stulecie
    if year <=1899:
        month = random.randint(1, 12) + 80
    elif 1900 <= year <= 1999:
        month = random.randint(1, 12)
    elif 2000 <= year <= 2099:
        month = random.randint(1, 12) + 20
    elif 2100 <= year <= 2199:
        month = random.randint(1, 12) + 40
    elif 2200 <= year <= 2299:
        month = random.randint(1, 12) + 60

    odd_month = (1, 3, 5, 7, 8, 10, 12, 21, 23, 25, 27, 28, 30, 32, 41, 43, 45, 47, 48, 50, 52, 61, 63, 65, 67, 68, 70, 72, 81, 83, 85, 87, 88, 90, 92)
    even_month = (4, 6, 9, 11, 24, 26, 29, 31, 44, 46, 49, 51, 64, 66, 69, 71, 84, 86, 89, 91)

    if month in odd_month:
        day = random.randint(1,31)
    elif month in even_month:
        day = random.randint(1,30)
    else:
        if (year % 4 == 0 and year != 1800 and  year != 1900 and year != 2100 and year != 2200):
            day = random.randint(1,28)
        else:
            day = random.randint(1,29)

    if (month <= 9):
        month = str(month)
        month = "0" + month
    else:
        month = str(month)

    if (day <= 9):
        day = str(day)
        day = "0" + day
    else:
        day = str(day)

    year = str(year)
    year = year[2] + year[3]

    four_random = random.randint(1000,9999)
    four_random = str(four_random)

    a = year[0]
    a = int(a)

    b = year[1]
    b = int(b)
    
    c = month[0]
    c = int(c)

    d = month[1]
    d = int(d)

    e = day[0]
    e = int(e)

    f = day[1]
    f = int(f)

    g = four_random[0]
    g = int(g)

    h = four_random[1]
    h = int(h)

    i = four_random[2]
    i = int(i)

    j = four_random[3]
    j = int(j)

    check = a + 3 * b + 7 * c + 9 * d + e + 3 * f + 7 * g + 9 * h + i + 3 * j

    if check % 10 == 0:
        last_digit = 0
    else:
        last_digit = 10 - (check % 10)

    last_digit = str(last_digit)

    return(year,month,day,four_random,last_digit)