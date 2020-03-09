import random # Importamos la clase random para los datos randomicos.
import time # Se importa la clase time, para saber el tiempo de ejecucion del programa.

# El siguiente es el método de ordenamiento QuickSort, acepta como parametro una lista (array), la cual es la 
# Traduccion de nuestros datos, almacenados por comas en un archivo.
def QuickSort(lista):
    # Las siguientes 3 listas, se utilizan para recorrer este arreglo y realizar las comparaciones.
    izquierda = []
    centro = []
    derecha = []
    # El siguiente condicional depende si nuestro arreglo contiene elementos.
    if len(lista) > 1:
        # La variable "pivote" se inicializa en el primer dato del array, y se utiliza para tener de ejemplo
        # ese dato, para compararlo con los demas, hasta hallar uno menor, igual o mayor:
        """ 
            1. Si el dato es menor se convertira en el nuevo pivote-
            2. Si el dato es igual, se coloca despues del pivote.
            3. Si el dato es mayor, debe ir despues del pivote.
        """
        pivote = lista[0]
        for i in lista: # Este ciclo for, recorre el array.
            # los siguiente condicionales realizan las comparaciones con respecto a nuestro pivote, con respecto
            # a los demas elementos que componen el array.
            if i < pivote:
                izquierda.append(i)
            elif i == pivote:
                centro.append(i)
            elif i > pivote:
                derecha.append(i)
        #print(izquierda+["-"]+centro+["-"]+derecha)
        return QuickSort(izquierda)+centro+QuickSort(derecha)
    else:
      return lista
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


# Impreción de los arreglos ordenados y no ordenados.
print ("No Ordenado \n")

print(files)

print ("Ordenado \n")

print(QuickSort(files))

hms = time.time()

# La siguiente linea expresa el tiempo de ejecucion
print((time.time()) - hms)

fr.close()