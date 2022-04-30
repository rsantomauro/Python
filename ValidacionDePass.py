listam = ["por favor","atento por favor", "media pila pibe", "estas de vivo", "Trampa!!!!"]

import time

contraseña = "123"

palabra=input("Por favor ingrese la contraseña: ")

intento = 0

while (palabra != contraseña) & (intento < 4):
    #print("Contraseña INCORRECTA!!!!")
    time.sleep(intento+1)
    palabra=input(str(listam[intento])+", ingrese la contraseña correctamente: ")
    intento=intento+1

if (palabra != contraseña) & (intento <= 5):
    print(listam[intento])

if (palabra == contraseña):
    print("Eureka!!!")