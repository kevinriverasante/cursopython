#definir una funcion max() que tome como argumento un
# array de numeros y devuelva el mayor del array
numeros=[23,45,67,12,34]
max=numeros[0]
for num in numeros:
    if num>max:
        max=num
print("el array mayor es "+str(max))
#escribir uan funcion que alamacene en una lista los seguientes precios,
#50,75,46,22,80,65,8, y muestre por pantalla el menor y ele mayor de los precios
precios=[50,75,46,22,80,65,8]
min=max=precios[0]
for precio in precios:
    if precio<min:
        min=precio
    elif precio>max:
        max=precio
print("el minimo precio es " + str(min))
print("el maximo precio es " + str(max))
#escribir una funcion mas_larga() que tome una array d palabras y devuelva la mas larga
palabras=["hola", "como estas","jose esta en el salon"]
min=max=palabras[0]
for palabra in palabras:
    if palabra<min:
        min=palabra
    elif palabra>max:
        max=palabra
print("la plabra mas larga es:"
      + str(max))
#ecribe un programa que reciba una cadena de carateres y devuelva un diccionario con cada palabra que contiene.
def creador_dict(cadena):
  '''Recibe una cadena de caracteres y regresa un diccionario con las palabras (keys) y conteo (value)'''
  lista_1= cadena.split()
  dict_1={}
  for i in lista_1:
    if i in dict_1:
      dict_1[i] +=1
    else:
      dict_1[i]= 1
  return dict_1

def contador_dict(dictionario):
  '''Recibe un diccionario y regresa una tupla: la palabra mas repetida y cuantas veces aparece'''
  palabra_frecuente= ''
  cantidad=0
  for keys,values in dictionario.items():
    if values > cantidad:
      cantidad= values
      palabra_frecuente= keys
  return palabra_frecuente,cantidad
entrada=input('Ingrese su cadena de caracteres: ')
print(creador_dict(entrada))
print(contador_dict(creador_dict(entrada)))
