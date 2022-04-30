#    Realizar un programa en python que muestre un menú  de 4 opciones que realicen las siguientes acciones:
#1)	Se pide por teclado nombre, cedula y edad, luego se guardan los datos en memoria, no se puede permitir que haya más de una persona con la misma cédula.
#2)	Se ordenan los datos por nombre alfabéticamente y se muestran.
#3)	Se ordenan los datos por edad de menor a mayor y se muestran
#4)	Salir del programa

#Cada punto del menú debe ser hecha con una función.
#Puede utilizar listas, diccionarios o combinación de ambas para guardar los datos.

# Funcion para la opcion 1 - Agrega cedula nombre y edad, comprar que la cedula no este duplicada
def opcion1tareas():
    cedula=0
    print("\n")
    while (cedula < 1):
        try:
            cedula=int(input("Ingrese cedula: "))
        except:
            print("La cedula ingresada es incorrecta")
    
    nombre=str(input("Ingrese nombre: "))
    edad=int(input("Ingrese edad: "))
    
    # Comparo cedula
    encontro= False
    for i in lista:
        if (cedula == i[0]):
            encontro= True
    
    if (encontro == False):
        lista.append([cedula,nombre,edad])
        clearConsole()
    else:
        print("La cedula ingresada ya existe\n")
    despliegoMenu()

# Funcion para la opcion 2    
def opcion2tareas():
    listaOrdenadaAlf= sorted(lista, key=lambda x:x[1])
    
    for x in range (0,len(listaOrdenadaAlf)):
        print(listaOrdenadaAlf[x][::])
    
    print("\n")
    despliegoMenu()

# Funcion para la opcion 3
def opcion3tareas():
    listaOrdenadaEdad= sorted(lista, key=lambda x:x[2])
    
    for x in range (0,len(listaOrdenadaEdad)):
        print(listaOrdenadaEdad[x][::])
    
    print("\n")
    despliegoMenu()
    
# Segun la opcion me dirijo a la funcion de la misma
def actionMenu(opcion):
    if (opcion == 1):
        opcion1tareas()
    
    if (opcion == 2):
        opcion2tareas()
        
    if (opcion == 3):
        opcion3tareas()
        
    if (opcion == 4):
        exit()

# Funcion para desplegar el menu
def despliegoMenu():
    print("Menu: ")
    print("1- Ingresar nombre, cedula y edad.")
    print("2- Ordenar datos por nombre.")
    print("3- Ordenar datos por edad de menor a mayor.")
    print("4- Salir")
    
    opcion=int(input("Ingresa una opcion del menu: "))
    while (opcion < 1 or opcion > 4):
        try:
            opcion=int(input("Ingresa una opcion del menu: "))
        except:
            depliegoMenu()
    
    actionMenu(opcion)

# Main
opcion= 0
lista=[]
clearConsole = lambda: print('\n' * 150)
despliegoMenu()