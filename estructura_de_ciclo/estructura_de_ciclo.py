#ESTRUCTURA DE CICLO
 #permite ejecutar funciones varias veces, estos son utilizados 
 #para determinar de una forma denamica en lugar de agregar la funcion n numeros de veces
 
 #for 
 #se inicializar variable que sera el contador, solo pasa por aqui al iniciar el ciclo var a =0;
 #se determina el numero de veces que se ejecutara el bloque de codigo a< 10;
 #se ejecutara cada vez que termine el bloque de codigo (mayormente se utiliza para aumentar o disminuir segun lo que se quiere hacer)
 
 #ejemplo1
 #for (var a = 0; a < 10; a++)
 #{
    #//bloque de codigo
    #console.log(a + "hola amigo");
 #}

 #ejemplo2
 #var x = 0, medida;
 #var dias= ["L", "M", "Mi", "J", "V"];
 #medida = dias.length;
   #for(; x < medida; x++)
 # {
    #console.log(dias[x]);
  #}
 #while tambien es estructura de ciclo

 #int es un metodo de python que transforma un dato
 #tipo texto a un dato de tipo numerico real o entero
 # input es un metodo de python que pide un dato
 #por consola al usuario
#condicion=True
#while condicion==True:
   #numero=int(input("ingresa el numero ganador:"))
   #if numero==10:
     #print("ganaste el premio")
     #condiciones=False
  # else:
    #print("ese no es el numero")

##crear un programa que me pida mi edad
#si engreso una edad incorrecta el programa
#seguira pidiendo mi edad
##si es la edad corrceta me mostrara un mensaje de correcto
#y se terminara la ejecucion
# condicion=True
# while condicion==True:
#    EDAD=int(input("ingresa su edad:"))
#    if EDAD==20:
#      print("tu edad es correcta")
#      condiciones=False
#    else:
#     print("ese no es tu edad")
##for

# password="71644288"
# for intentos in range(1,4):
#     print("este es tu",intentos,"intento")
#     newpassword=input("ingresa el password correcto:")
#     if newpassword==password:
#         print("bienvenido joven")
#         break
#     else:
#         print("contraseña incorrecta sigue intentando")
# password="71644288"
# condicion=True
# intentos=1

# ##while
# while condicion==True:
#     print("este es tu",intentos,"intentos")
#     newpassword=input("ingresa el password correcto:")
#     if newpassword==password:
#         print("bienvenido al sistema joven")
#         condicion=False
#     else:
#         print("eres un gil")
#         intentos+=1

# condicion=True
# eval=1
# while condicion==True:
#     if eval==5:
#         print("estamos en 5")
#         condicion=False
#     else:
#         eval+=1
# ##tabla de multiplicar con for
# for numeros in range(1,11):
#     print(numeros,'*',2,'=',numeros*2)
# ##tabla del numero que quieres
# numero=int(input("ingrese el numero de la tabla que desee mostrar:"))
# for numeros in range(1,11):
#     print(numeros,'*',numero,'=',numeros*numero)
# ##que siga pediendo la tabla
# eval=True
# while eval==True:
#     numero = int(input("ingrese el numero de la tabla que desee mostrar:"))
#     if numero==0:
#         print("error saliendo del programa....")
#         break
#     else:
#         for numeros in range(1, 11):
#             print(numeros, '*', numero, '=', numeros * numero)

##
# if numero==0:
#     for numeros in range(1, 11):
#         print(numeros, '*', numero, '=', numeros * numero)
# else:
#     print("error saliendo del programa....")
#     break

##
##mensaje="hola"
##print(mensaje[3])
##for letra in mensaje:
    ##print(letra)

##mostrar por consola cuantas vocales a
##tiene el mensaje

# mensaje=input("ingresa un mensaje:")
# contador=0
# for letra in mensaje:
#     if letra=="a":
#         contador+=1
# print("en este mensaje tienes",contador,"letras a")

##escribir un progrma que muestre el eco de
#todo lo qe el usuario intruduzca hasta que el usuario escriba "salir"
#que terminara

# while True:
#     mensaje = input("Escriba el eco: ")
#     if mensaje == "salir":
#         break
#     print(mensaje)
#de otra forma

# palabra=""
# while palabra!="salir":
#     palabra=input("escribe algo: ")
#     print(palabra)
##utelizando for
# contador=10
# for num in range(0,contador):
#     palabra=input("ingresa algo: " )
#     if palabra=="salir":
#         break
#     contador+=1

##vocales en una oracion
#oracion=input("ingrese su oracion")
#vocales=["a","e","i","o","u"]
#contadorvocales=0
#for letras in oracion:
 #   if letras in vocales:
  #      contadorvocales+=1
#print("la cntidad de vocales es:",contadorvocales)

##

# sentence=input("ingrese una oracion: ")
# handlervocals=0
# for words in sentence:
#     match words:
#         case "a":
#             handlervocals+=1
#         case "e":
#             handlervocals+=1
#         case "i":
#             handlervocals+=1
#         case "o":
#             handlervocals+=1
#         case "u":
#             handlervocals+=1
# print("la cantidad de vocales es:",handlervocals)
##
opcion = 0
while True:
    print("""
    Dime, ¿qué quieres hacer?

    1) Sumar los dos números
    2) Restar los dos números
    3) Multiplicar los dos números
    4) Cambiar los números elegidos
    5) salir
    """)
    opcion = int(input("Elige una opción: "))
    n1 = float(input("Introduce tu primer número: "))
    n2 = float(input("Introduce tu segundo número: "))
    if opcion == 1:
        print(" ")
        print("RESULTADO: La suma de", n1, "+", n2, "es igual a", n1 + n2)
    elif opcion == 2:
        print(" ")
        print("RESULTADO: La resta de", n1, "-", n2, "es igual a", n1 - n2)
    elif opcion == 3:
        print(" ")
        print("RESULTADO: El producto de", n1, "*", n2, "es igual a", n1 * n2)
    elif opcion == 4:
        n1 = float(input("Introduce tu primer número: "))
        n2 = float(input("Introduce tu segundo número: "))
    elif opcion == 5:
        break
    else:
        print("Opción incorrecta")
###
mensajeOpciones="""
================================
selecciona una opcion
 1)suma
 2)resta
 3)divicion
 4)multiplicacion
 5)salir
================================
"""
while True:
    print(mensajeOpciones)
    opcion=input("ingresa una opccion valida entre(1-5):")
    num1=int(input("ingrese el primer numero"))
    num2=int(input("ingrese el segundo numero"))
    match opcion:
        case "1":
            print(f"la suma de {num1}+{num2}={num1+num2}")
        case "2":
            print(f"la resta de {num1}-{num2}={num1-num2}")
        case "3":
            print(f"la divicion de {num1}/{num2}={num1/num2}")
        case "4":
            print(f"la multiplicacion de {num1}*{num2}={num1*num2}")
        case "5":
            break
        case _:
            print("esta opcion no exixte")

###
def operaciones(num1,num2,operacion):
    return
mensajeOpciones="""
================================
selecciona una opcion
 1)suma
 2)resta
 3)divicion
 4)multiplicacion
 5)salir
================================
"""
while True:
    print(mensajeOpciones)
    opcion=input("ingresa una opccion valida entre(1-5):")
    num1=int(input("ingrese el primer numero"))
    num2=int(input("ingrese el segundo numero"))
    operaciones(num1,num2,opcion)





