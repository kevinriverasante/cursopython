##aqui creare mis funciones
def operaciones(numero1,numero2,operador):
    if operador=="suma":
        total=numero1+numero2
    if operador=="resta":
        total=numero1-numero2
    if operador=="multiplicacion":
        total=numero1*numero2
    if operador=="divicion":
        total=numero1/numero2
    return total
def saludo():
    mensaje="hola alumnitos bellos"
    return mensaje