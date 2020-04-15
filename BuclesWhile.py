i=1
while i<=10:
    print("ejecucion" + str(i))
    i=i+1
print("termino la ejecucion")
#ejemplo2

edad=int(input("Introduce la edad "))
while edad<5 or edad>100:
    print("Has introducido una edad negativa. VUelve a intentar")
    edad=int(input("Introduce la edad "))
print("gracias por colaborar.Puedes pasar")
print("Edad del aspirante "+str(edad))