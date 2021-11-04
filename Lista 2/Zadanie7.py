list=[(2,8),(5,5),(9,3),(1,0),(3,2),(6,4),(1,9),(10,3),(2,3),(1,7)]
print("przed sortowaniem: ")
print(list)
print("po sortowaniu: ")
list.sort(key=lambda x: x[1]) #funckja z internetu w sensie klucz
print(list)