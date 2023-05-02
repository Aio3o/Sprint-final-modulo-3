import random

personas=["alejandro", "miguel", "william", "anastasia", "claudia", "nicole", "alex","elizabeth","cindy","ana"]
cuentas=[]
letras="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
numeros="123456789"
numlet=f"{letras}{numeros}"
for persona in personas:
    while True:
        numero="0"
        while len(numero)!=8:
            numero=input("Ingrese numero para "+persona+" :" )
            if len(numero) !=8:
                print("El numero debe contener 8 digitos")
        try:
            numero=int(numero)
        except:
            print("Ingrese un número valido")
        else: 
            break   
    gencontra=random.sample(numlet,8)
    contra= "".join(gencontra)
    cuentas.append({"nombre":persona,"contraseña":contra,"número":str(numero)})
print(cuentas)