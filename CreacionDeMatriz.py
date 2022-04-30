numeros=-1
while (numeros < 1):
    try:
        numeros=int(input("Ingrese un numero: "))
    except:
        print("error")

matriz=[]
    
for i in range (1,numeros+1):
    matriz.append([])
    for j in range (i,numeros+1):
        matriz[i-1].append(j)
    for l in  range (1,i):
        matriz[i-1].append(l)
for x in range (0,numeros):
    print(matriz[x][::])