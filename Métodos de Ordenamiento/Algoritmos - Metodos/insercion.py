import random # Importamos la clase random para los datos randomicos.
import time # Se importa la clase time, para saber el tiempo de ejecucion del programa.

# El siguiente método de ordenamiento se encarga de tomar como parametro una lista.
def ordenamientoPorInsercion(unaLista):
   for indice in range(1,len(unaLista)): # Este ciclo for, recorre la lista en un rango desde 1 hasta la longitud.
    # La variable "valorActual", sirve como varible temporal, para saber que dato tenemos en esa posicion.
     valorActual = unaLista[indice]
     posicion = indice
    # El siguiente ciclo while se utiliza para insertar los valores, con ayuda de un operador lógico, denominado, 
    # "and", para que cumpla ambas condiciones y se pueda ordenar la lista.
     while posicion>0 and unaLista[posicion-1]>valorActual:
         unaLista[posicion]=unaLista[posicion-1]
         posicion = posicion-1

     unaLista[posicion]=valorActual
#Escribe numeros en un archivo llamado "Ejemplo.txt"

File = open("Ejemplo.txt", "w")
for i in range(10): # Se utiliza el ciclo for, para llenar el archivo con los datos randomicos 
    # y separados por comas.
  File.write( str(random.randint(1,1000)) + "," ) # La función Write se utiliza para escribir sobre el archivo, 
  # teniendo en cuenta que estan separados por comas.

File.close() # La función Close, se utiliza para cerrar el archivo sobre el cual se esta escribiendo.

# Leer y sumar los numeros del archivo "Ejemplo.txt"
fr = open("Ejemplo.txt", "r")
for line in fr: # El ciclo for en este caso, se utiliza para leer los datos y las lineas del archivo.
  files = line.split(",") # El Método Split se encarga de leer solamente los datos, que no sean comas (,).

tam = len(files)-1 # Len sirve para obtener la longitud.

# Impreción de los arreglos ordenados y no ordenados.
print ("No Ordenado \n")

print(files)

print ("\nOrdenado \n")

ordenamientoPorInsercion(files)
print(files)

hms = time.time()

# La siguiente linea expresa el tiempo de ejecucion
print((time.time()) - hms)

fr.close()