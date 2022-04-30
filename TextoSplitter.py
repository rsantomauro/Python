texto="  esto      es un    prueba  bien rara"
lista=texto.split(" ")
for i in range (len(lista)-1, -1, -1):
    if (lista[i] == " " or lista[i] == ""):
        lista.pop(i)
print(lista)