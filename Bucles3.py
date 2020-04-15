for i in range(5):
    print(i)
    print(f"valor de la variable {i}")


#ejemplo 2
for i in range(5,10):
    print(i)
    print(f"valor de la variable {i}")
#ejemplo 3
for i in range(5,50,3):
    print(i)
    print(f"valor de la variable {i}")

#ejemplo 4

valido=False
email=input("INtroduce tu email: ")
for i in range(len(email)):
    if email[i]=="@":
        valido=True

if valido:
    print("Email correcto")
else:
    print("Email incorrecto")
