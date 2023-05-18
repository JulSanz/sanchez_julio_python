
#input de frase
Frase = input("Ingresa tu frase: ")

#funcion que genera diccionario
def palabras_longitud(Frase):
    palabras = Frase. split()
    diccionario = {}
    
#contar len por cada palabra
    for palabra in palabras:
        diccionario[palabra] = len(palabra)

    return diccionario

print(palabras_longitud(Frase))


