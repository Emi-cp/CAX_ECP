frutas=["aguacate","melon","tomate","berenjena","zarzamora"]

print(frutas)

print(len(frutas))

print(frutas[2])

frutas.append("papaya")
print(frutas)

frutas.append("sandía")
print(frutas)

frutas.sort()
print(frutas)

compra=input("Ingresa una fruta: ")
frutas.append(compra)

print(frutas)

print(dir(frutas))