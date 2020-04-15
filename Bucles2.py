for i in ["Pildoras","Informaticas",3]:
    print("Hola",end="  ")


#ejemplo 2

for i in "juan@pildorasinformaticas.com":
    print("Hola",end=" ")
#ejemplo3

email=False

for i in "juan@pildorasinformaticas.com":
    if (i=="@"):
        email=True

if email==True:
    print("email es correcto")
else:
    print("el email es incorrecto") 
#ejemplo 4
miEmail=input("Introduce tu direccion de email: ")
email=False
for i in miEmail:
    if (i=="@"):
        email=True
if email==True:
    print("El email es correcto")
else:
    print("El email es incorrecto")
#ejemplo 5 con contador
contador=0
miEmail=input("Introduce tu direccion de email: ")
for i in miEmail:
    if(i=="@" or i=="."):
        contador=contador+1
if contador==2:
    print("Email es correcto")
else:
    print("Email es incorrecto")


