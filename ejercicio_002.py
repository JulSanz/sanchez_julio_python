nombre = input("Ingresa tu Nombre ")
sexo = input("Ingresa tu sexo M/F ")


nombreupper = nombre.upper()

if (sexo == "M" and nombreupper >= "N") or (sexo == "F" and nombreupper < "M"):
    print("Grupo A")
else:
    print("Grupo B")


print(nombreupper)


