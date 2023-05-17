#Entrada de Paswword
password_master = input(" Crea tu password ")


#Ciclo para validar password
while True:
    #Pedir nuevo pasword, tiene que estar dentro del bucle para que no se retroalimente
    password_request = input(" Ingresa tu password ")
    #Condicional
    if password_master == password_request:
        print("Bienvenido")
        break
    else: 
        print("Tu Password no es correcto")
