##llamando la funcion
##aqui en main ejecutare mis funciones
##from funciones import operaciones
import funciones as op
respuesta=op.operaciones(10,8,"suma")
respuesta2=op.operaciones(100,20,"resta")
respuesta3=op.operaciones(5,10,"multiplicacion")
print(f"la suma es {respuesta}")
print(f"la suma es {respuesta2}")
print(f"la multiplicacion es {respuesta3}")
###
print(op.saludo())