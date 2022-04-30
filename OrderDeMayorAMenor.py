def menores_y_mayores(lista, valor):
    menores = []
    mayores = []
    for num in lista:
        if (num > valor):
            mayores.append(num)
        else:
            if (num < valor):
                menores.append(num)
    return menores, mayores

lista = [10, 20, 30, 60, 109.3, 100, 30, 60, 90, 100, 150, 200]
valor = 100

print("Lista a obtener los valores menores y mayores a {}:{}.".format(valor, lista))

unicaMenores = []
unicaMayores = []

menores, mayores = menores_y_mayores(lista, valor)

for valor in menores:
    if valor not in unicaMenores:
        unicaMenores.append(valor)

for valor in mayores:
    if valor not in unicaMayores:
        unicaMayores.append(valor)

print("\nValores menores a {}: {}. Valores mayores a {}:{}".format(valor, unicaMenores, valor, unicaMayores))
