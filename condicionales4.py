#Condicionales 4
print("Programas de becas a;o 2017")
distacia_escuela=int(input("Introduce la distancia a la escuela en km "))
print(distacia_escuela)

numero_hermanos=int(input("Introduce numero de hermanos en el centro "))
print(numero_hermanos)

salario_familiar=int(input("Introduce salario anual bruto "))
print(salario_familiar)

if distacia_escuela>40 and numero_hermanos>2 and salario_familiar<=20000:
    print("Tienes derecho a beca")
else:
    print("NO tienes derecho a beca")