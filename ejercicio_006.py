#Constante
import math
pi = math.pi


#Funcion para Area
def area_circulo (radio):
    areacic = pi * radio ** 2
    return areacic

#funcion para volumen
def area_cilindro (radio , altura):
    area_base = area_circulo(radio)
    volumencil = area_base * altura
    return volumencil

#Pedir radio
radio = float(input("Cual es el radio del circulo? "))
area = area_circulo(radio)
print("El area del circulo es: ", round(area,2), "metros cuadrados")

#Pedir Altura
altura = float(input("Cual es la altura del cilindro? "))
volumen = area_cilindro(radio, altura)
print("El volumen del cilindro es: ", round(volumen,2) , "metros cubicos")

