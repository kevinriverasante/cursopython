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

condicion=True
eval=1
while condicion==True:
    if eval==5:
        print("estamos en 5")
        condicion=False
    else:
        eval+=1

