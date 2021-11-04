text = "restart"
print(text[0] + text[1:].replace(text[0], "$"))
text = input("Podaj słowo jakieś inne: ")
print(text[0] + text[1:].replace(text[0], "$"))