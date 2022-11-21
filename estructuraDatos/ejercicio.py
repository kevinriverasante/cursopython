##escribe una funcion en python quen acepte uan lista y genere otra lista eliminando
#los duplicados numeros
def datos():
    datos = [1, 1, 2, 2, 3, 4, 4, 5, 6,6]
    result = []
    for item in datos:
        if item not in result:
            result.append(item)
    return result
##escriba uan funcion que acepte una lista y genere otra con los numeros pare
def numpar(array):
    newArray=[]
    sarai=set(array)
    for n in sarai:
        if n % 2==0:
            newArray.append(n)
    return newArray
arrayA=[1,1,2,2,3,3,4,4,5,5,6,6,6,7]

##escribe uan funcion que acepte una lista y genere otra lista eliminando los textos dulicados
def texto():
    data = ["hola","hola","como estas","como estas"]
    result = []
    for item in data:
        if item not in result:
            result.append(item)
    return result
##escribir una funcion qe acepte una lista y genere otra lista mostrarndo numeros primos

