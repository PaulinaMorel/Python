def check(pesels):
    
    a = pesels[0]
    a = int(a)

    b = pesels[1]
    b = int(b)

    c = pesels[2]
    c = int(c)

    d = pesels[3]
    d = int(d)

    e = pesels[4]
    e = int(e)

    f = pesels[5]
    f = int(f)

    g = pesels[6]
    g = int(g)

    h = pesels[7]
    h = int(h)

    i = pesels[8]
    i = int(i)

    j = pesels[9]
    j = int(j) 

    k = pesels[10]
    k = int(k)

    check = a + 3 * b + 7 * c + 9 * d + e + 3 * f + 7 * g + 9 * h + i + 3 * j

    if check % 10 == 0:
        last_digit = 0
    else:
        last_digit = 10 - (check % 10)


    if last_digit == k:
        return True
    else:
        return False

def pesel_info(pesels):
    month = int(pesels[2] + pesels[3])
    #int_month = int(month)
    
    year_1800 = (81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92)
    year_1900 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
    year_2000 = (21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32)    
    year_2100 = (41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52)
    year_2200 = (61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72)

    year = int(pesels[0] + pesels[1])
    #int_year = int(year) 
    if month in year_1800:
        year = year + 1800
    if month in year_1900:
        year = year + 1900
    if month in year_2000:
        year = year + 2000
    if month in year_2100:
        year = year + 2100
    if month in year_2200:
        year = year + 2200    

    year = str(year)
    month = pesels[2] + pesels[3]
    day = pesels[4] + pesels[5]
    
    gender_number = int(pesels[9])
    if (gender_number % 2) == 0:
        gender = "k"
    else:
        gender = "m"

    return year, month, day, gender