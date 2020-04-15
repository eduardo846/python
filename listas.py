#Listas en python 
milista=["Maria","Pepe","Marta","Antonio"]
print(milista[:])
print(milista[0])
print(milista[0:3])


#Agregar elementos a una lista
milista.append("Sandra")
print(milista)
#Agragar una nueva matriz
milista.extend(["Sandra1","Sandra2"])
print(milista)
#Buscar el index o po9icion de un elemeto 
print(milista.index("Pepe"))
#Se encuentra o no un elemento TRUE O FALSE
print("Pepe" in milista)
#ELIMINAR ELEMENTO
milista.remove("Maria")
print(milista[:])
#eliminar el ultimo elemento
milista.pop()
