# Función que reciba 2 listas, una con claves (cedulas) y otra con nombres de alumnos.
# Retorna un diccionario con eso.
# Reciba una cedula y diga si el alumno está o no esta, si esta tiene que decir cuál es.

def crear_diccionario(cedulas,nombres):
    diccionario = {}
    paso = 0
    for cedula in cedulas:
        diccionario[cedula]= str(nombres[paso])
        paso = paso +1
    return diccionario

cedulas = ["12345678", "123456788", "98765432", "74561237", "75342159"]
nombres = ["Pepe", "Ramon", "Jorge", "Paco", "Ana"]

diccionario=crear_diccionario(cedulas,nombres)

consulta=input("Ingrese una cedula para consultar: ")

if (consulta in diccionario):
    print("El alumno es " + str(diccionario.get(consulta)))
else:
    print("El alumno no esta.")