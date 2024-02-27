import pandas as pd 
import math
import statistics
while (True):
    print("""Bienvenido al Menu interactivo:
    1)Calcular el promedio de la variable propiedadepm
    2)Calcular el total de la variable propiedadepm
    3)total de la variable propiedadepm y compartido""")
    opcion=input("introduce una de las siguientes opciones:")
    datos = pd.read_csv('C:/Users/ASUS/OneDrive/Escritorio/trabajoprogramacion/data.csv',sep=';', engine='python', error_bad_lines=False, warn_bad_lines=False) #lea el archivo csv (coloque 'r' antes de la cadena de ruta para abordar cualquier carácter especial en la ruta, como como '\'). No olvides poner el nombre del archivo al final de la ruta + ".csv" 
    if opcion == "1":
        print("El promedio de la Variable propiedadepm es :",statistics.mean(datos["propiedadepm"]))
    elif opcion == "2":
        print("El total de la variable propiedadepm es :", math.fsum(datos["propiedadepm"]))
        if opcion == "3":
            print("El total de la variable propiedadepm es :", math.fsum(datos["compartido"]))
        break
    else:
        print("Has ingresado una opcion incorrecta")

