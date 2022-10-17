#ESTRUCTURA DE DECISION

#if: por ejemplo que la nota para aprobar es 60. la sentencia en pseudocodigo es la siguiente:
    
 #si el estudiante obtiene una nota igual o superior a 60:
   #aprobado
 #si la condicion es verdadera, se imprime "aprobado", si la condicion es falsa, la sentencia de impresion es ignorada
 #ejemplo:
#  if nota >= 60:
#     print("aprobado")
#if/else y if/elif/else: la estructura de decision actua solo cuando la condicion es verdadera, de lo contrario la accion se ignora.
 #la estructura if/else permite al programador epecificar que una accion diferente se debe desarrollar, cuando la condicion es falsa.
 #por ejemplo

 #si el estudiante obtiene una nota igual o superior a 50:
 #entonces:
    #APROBADO
 #si no
    #SUSPENDIDO
 
#  if nota >= 60:
#     print("aprobado")
#  else:
#     print("suspendido")

#  #tambien se utiliza de seleccion multiple if/elif/else.
#   if nota >= 80:
#     print("A")
#   elif nota >= 70:
#     print("B")
#   elif nota >= 60:
#     print("C")
#   elif nota >= 50:
#     print("D")
#   else:
#     print("F")

# operacion="resta"
# match operacion:
#   case "suma":
#     print("realizare una suma")
#   case "resta":
#     print("realizare una resta")
#   case "multiplicacion":
#     print("realizare una multiplicaccion")
#   case _:
#     print("no hay operacion")

##tendremos una variable con el mensaje hola mundo
#pedimos al usuario un texto
##si el texto ingresado es hola
##mostraras el mensaje completo
## si el texto ingresado es como estas
##estraeras del mensaje la palabra hola
##si el texto ingresado es saludos
##estraeras el palabra mundo
##si se ingresa otro texto
##mostraras por defecto el mensaje de error


# mensaje="hola mundo"
# texto=input("ingresa un texto:")
# match texto:
#    case "hola":
#      print(mensaje[:])
#    case "como estas":
#      print(mensaje[:4])
#    case "saludos":
#      print(mensaje[5:])
#    case _:
#     print("error")

##convertir match a if
mensaje="hola mundo"
texto=input("ingresa un texto:")
if texto:
  if texto=="hola":
    print(mensaje[:])
  elif texto=="como estas":
    print(mensaje[:4])
  elif texto=="saludos":
    print(mensaje[5:])
  else:
    print("error")