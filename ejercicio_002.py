#Definir entradas
nombre = input("Ingresa tu Nombre ")
sexo = input("Ingresa tu sexo M/F ")

#Validacion de texto mayusculas
nombreupper = nombre.upper()


#Condicional para dividir grupos
if (sexo == "M" and nombreupper >= "N") or (sexo == "F" and nombreupper < "M"):
    print("Grupo A")
else:
    print("Grupo B")


print(nombreupper)


