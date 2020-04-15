def generarPares(limite):

    num=1
    milista=[]

    while num<limite:
        yield num*2
        num=num+1
devuelvePares=generarPares(10)
#for i in devuelvePares:
   # print(i)
print(next(devuelvePares))
print("Aqui pdria ir mas codigo")
print(next(devuelvePares))
print("Aqui pdria ir mas codigo")
print(next(devuelvePares))
