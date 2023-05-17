#Diccionario frutas + precio
dicfrutas = {
    "Platano" : 1.35 , 
    "Manzana" : .8,
    "Pera" : .85,
    "Naranja" : .7
}

#definir disponibles
print("Estas frutas estan disponibles:")
for x in dicfrutas:
    print(x)

#datos entrada
entradafruta = input("Cual fruta quieres?")
entradakg = float(input("Cuantos kilos llevas?"))

#validacion a entrada
if entradafruta in dicfrutas:
    print(entradakg, "kilos de", entradafruta, "cuestan $", dicfrutas[entradafruta]*entradakg)
else:
    print(entradafruta, "no esta disponible")
