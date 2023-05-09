password_master = input(" Crea tu password ")



while True:
    password_request = input(" Ingresa tu password ")
    if password_master == password_request:
        print("Bienvenido")
        break
    else: 
        print("Tu Password no es correcto")
