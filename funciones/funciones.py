#averiguar sobre funciones
#líneas de código que realizan una tarea específica y pueden tomar
#“Argumentos” para diferentes “Parámetros” que modifiquen su funcionamiento y los datos de salida. 
# def multiplica_por_7(numero):
#     print(f'{numero}+7 = {numero + 7}')
# print("comienzo del programa ")
# multiplica_por_7(7)
# print("seguiente")
# multiplica_por_7(113)
# print("fin")
##la funcion multiplica_por_7() define un parametro llamado numero que es lo que se uteliza para multiplicar por 5
##el resultado del programa anterior seria el siguiente:
#comienzo del programa
 #7*7 = 49
 #seguiente
 #113*7 = 791
 #fin
#el programa comienza su ejecucion en la line 6 y va ejecutando las instrucciones una a una de manera ordenada
#cuando se encuentra el nokmbre de la funcion "multiplica_por_7(), el flujo de ejecucion pasa a la primera instruccion
#de la funcion.cuando se llega a la instruccion de la funcion; el flujo del programa sigue por la instruccion que hay a continuacion
#de la llamada de funcion.

##funcines
##2 tipos de funciones
##funciones propias de python
#print(parametros)##mostrar mensaje o resultado
#int(parametros)##esta funcion sirve paar convertir string en entero
#input(parametros)##esta funcion sirve para pedir datos al usuario
##todo lo que se ingrese en input sera tomado como texto

##funciones creadas

# def saludo(a,b):
#     resultado=a+b
#     return resultado
##uso de funcion
# print(saludo(3,6))

# numero="10" ##10
# int(numero)##10
##int es el nombre de la funcion
##() y dentro de parentesis van los parametros

# sentence=input("ingrese una oracion: ")
# def countvocals(texto):
#     vocales=["A","e","i","o","u"]
#     contadorvocales=0
#     for letras in texto:
#         if letras in vocales:
#             contadorvocales+=1
#     return contadorvocales
# print("la cantidad de vocales es:",countvocals(sentence))

##crear un afuncion de operaciones matematicas
##operadormatematico(numerouno,numerodos.numerodos,operacion)
##operadormatematico(4,5,"entre")
##por consola la suma de 4/5
#=======================================
# def operaciones(num1,num2,operacion):
#     if operacion=="suma":
#         operaciones="la suma de: ",num1,"+",num2, "es ",num1+num2
#     elif operacion=="resta":
#         operaciones="la resta de: ",num1,"-",num2, " es ",num1-num2
#     elif operacion=="multiplicacion":
#         operaciones="la multiplicacion de: ", num1, "*", num2, "es", num1*num2
#     elif operacion=="divicion":
#         operaciones="la divicion de: ", num1, "/", num2, "es", num1/num2
#     return operaciones
# print(operaciones(10,5,"divicion"))
#================================

# def mensaje(nombre,apellido,accion):
#     if accion== "saludo":
#         mensaje="hola",nombre,apellido,"como estas"
#     elif accion == "despedida":
#         mensaje="adios",nombre,apellido
#     return mensaje
# print(mensaje("jose","alvarez","saludo"))

##vocales en una oracion
#==================================
# sentence=input("enter sentence: ")
# vocales=["a","e","i","o","o"]
# def countvocal(oracion,vocal):
#     contador=0
#     for word in oracion:
#         if word in vocal:
#             contador+=1
#     return contador
# print(countvocal(sentence,vocales))
#=========================================
#1 uetelizar la palabra reserva def
#2. asisgnamos un nombre a la funcion--descriptivo
#3 siempre tiene que recibir parametros
 #()----no sirve parametros
 #(nombre)----que una funcion esat recibiendo un parametro
 ##(edad,nokbre)
 #4 siemopre la funcion tiene que retornar un tipo de dato
# def saludo(nombre):
#     respuesta=f"hola como estas {nombre}"
#     return respuesta
#  ##como uso
# arrayamigos=["ronal","claudio","diego","jose","mozar","kevin","lilian"]
# for amigo in range(0,len(arrayamigos)):
#     print(saludo(arrayamigos[amigo]))

##crea una funcion que me retorne los n numeros fibonacci
###
# def fib(n):
#     if n <2:
#         return n
#     return fib(n-1)+fib(n-2)
# for x in range(20):
#     print(fib(x))
##crear una funcion que me retorne el factorial de un numero n
#5=5*4*3*2*1
#7=7*6*5*4*3*2*1
# numero=int(input("numero: "))
# factorial=1
# if numero!=0:
#     for i in range(1,numero+1):
#         factorial=factorial*1
# print("factorial: ",factorial)
##crear una funcion que me diga si una palabra es palindromo
#ada
#ala
#reconocer
letra=input("ingresa la palabra: ")
if (letra)==(letra)[::-1]:
    print("es palindromo")
else:
    print("no es palindromo")

