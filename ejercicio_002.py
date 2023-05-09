nombre = input("Ingresa tu Nombre ")
sexo = input("Ingresa tu sexo M/F ")




if (sexo == "M" and nombre >= "N") or (sexo == "F" and nombre < "M"):
    print("Grupo A")
else:
    print("Grupo B")


