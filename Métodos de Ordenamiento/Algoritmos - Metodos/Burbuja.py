import random # Importamos la clase random para los datos randomicos.
import time # Se importa la clase time, para saber el tiempo de ejecucion del programa.

# El siguiente método es el ordenamiento burbuja y recibe como parametro la lista que conforma el archivo.
def ordenamientoBurbuja(unaLista):
  # Los siguientes ciclos for, se implementan para recorrer el arreglo, que contiene los datos 
  # almacenados por el archivo.
    for numPasada in range(len(unaLista)-1,0,-1):
        for i in range(numPasada):
            # El condicional if se utiliza para realizar las comparaciones entre los datos.
            if unaLista[i]>unaLista[i+1]:
                temp = unaLista[i]
                unaLista[i] = unaLista[i+1]
                unaLista[i+1] = temp


#Escribe numeros en un archivo llamado "Ejemplo.txt"

File = open("Ejemplo.txt", "w")
for i in range(100): # Se utiliza el ciclo for, para llenar el archivo con los datos randomicos 
    # y separados por comas.
  File.write( str(random.randint(1,1000)) + "," ) # La función Write se utiliza para escribir sobre el archivo, 
  # teniendo en cuenta que estan separados por comas.

File.close() # La función Close, se utiliza para cerrar el archivo sobre el cual se esta escribiendo.

# Leer y sumar los numeros del archivo "Ejemplo.txt"
fr = open("Ejemplo.txt", "r")
for line in fr: # El ciclo for en este caso, se utiliza para leer los datos y las lineas del archivo.
  files = line.split(",") # El Método Split se encarga de leer solamente los datos, que no sean comas (,).

tam = len(files)-1 # Len sirve para obtener la longitud.

"""suma = 0
for j in range(tam):
  suma += int(files[j])
print(suma)"""

# Impreción de los arreglos ordenados y no ordenados.
print ("No Ordenado \n")

print(files)

print ("Ordenado \n")
ordenamientoBurbuja(files)
print(files)

hms = time.time()

# La siguiente linea expresa el tiempo de ejecucion
print((time.time()) - hms)

fr.close()