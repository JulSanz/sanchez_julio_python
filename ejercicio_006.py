#Constante
import math
pi = math.pi


#Funcion para Area
def area_circulo (radio):
    return  pi * radio ** 2

#funcion para volumen
def area_cilindro (radio , altura):
    area_base = area_circulo(radio)
    return area_base * altura

#Pedir radio
radio = float(input("Cual es el radio del circulo? "))
area = area_circulo(radio)
print("El area del circulo es: ", round(area,2), "metros cuadrados")

#Pedir Altura
altura = float(input("Cual es la altura del cilindro? "))
volumen = area_cilindro(radio, altura)
print("El volumen del cilindro es: ", round(volumen,2) , "metros cubicos")
