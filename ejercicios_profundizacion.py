#!/usr/bin/env python
'''
Numpy [Python]
Ejercicios de profundización
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import numpy as np
import random
import math
import re


lista_jugador1 = []
lista_jugador2 = []
suma_jugador1 = []
suma_jugador2 = []


def ej1():
    print('Comenzamos a divertirnos!')

    '''
    Empecemos a jugar con las listas y su métodos, el objetivo
    es realizar el código lo más simple, ordenado y limpio posible,
    no utilizar bucles donde no haga falta, no "re inventar" una función
    que ya dispongamos de Python. El objetivo es:

    1) Generar una lista 3 numéros aleatorios con random (pueden repetirse),
       que estén comprendidos entre 1 y 10 inclusive
       (NOTA: utilizar comprension de listas a pesar de poder hacerlo
        con un método de la librería random)
    2) Luego de generar la lista sumar los números y ver si el resultado
       de la suma es menor o igual a 21
       a) Si el número es menor o igual a 21 se imprime en pantalla
          la suma y los números recoletados
       b) Si el número es mayor a 21 se debe tirar la lista y volver
          a generar una nueva, repetir este proceso hasta cumplir la
        condicion "a"

    Realizar este proceso iterativo hasta cumplir el objetivo
    '''
    
    lista_numeros = [random.randint(1, 11) for x in range(3)]
    
    while True:
        suma = sum(lista_numeros)
    
        if  suma <= 21:
            # Inove: En este caso se est copiando tal cual lista_numeros a lista_recolectados
            # en caso de ser necesario lista_recolectados se puede generar directamente como:
            # lista_recolectados = lista_numeros
            lista_recolectados = [x for x in lista_numeros if suma <= 21] 
            print('Suma:', sum(lista_recolectados), ', de la lista:', lista_recolectados)
            break
            
        elif suma > 21:
            lista_numeros = [random.randint(1, 11) for x in range(3)]


def ej2():
    print('Comenzamos a ponernos serios!')

    '''
    Dado una lista de nombres de personas "nombres" se desea
    obtener una nueva lista filtrada que llamaremos "nombres_filtrados"
    La lista se debe filtrar por comprensión de listas utilizando la
    lista "padron" como parámetro.
    La lista filtrada solo deberá tener aquellos nombres que empiecen
    con alguna de las letras aceptadas en el "padron".
    '''

    padron = ['A', 'E', 'J', 'T']

    

    nombres = ['Tamara', 'Marcelo', 'Martin', 'Juan', 'Alberto', 'Exequiel',
               'Alejandro', 'Leonel', 'Antonio', 'Omar', 'Antonia', 'Amalia',
               'Daniela', 'Sofia', 'Celeste', 'Ramon', 'Jorgelina', 'Anabela']

    # Se espera obtener:
    # ['Tamara', 'Juan', 'Alberto'......]


    nombres_filtrados = [x for x in nombres if x[0] == padron[0] or x[0] == padron[1] or x[0] == padron[2] or x[0] == padron[3]]
    
    # Inove: Una opción para no tener que probar contra todos los elementos de la lista si este elemento se encuentra
    # incluido es utilizar el operador "in". El operador "in" se utilizar para entender si un elemento se encuentra
    # contenido dentro de otro (en este caso si la primera letra del nombre se encuentra incluida entre las del padron
    # nombres_filtrados = [x for x in nombres if (x[0] in padron)]
    
       
    print(nombres_filtrados)

def ej3():
    print("Un poco de Numpy!")
    # Ejercicio de funciones
    # Se desea calcular los valores de salida de
    # una función senoidal, dado "X" como el conjunto
    # de valores que deben someter a la función "sin"

    # Conjunto de valores "X" en un array
    x = np.arange(0, 2*np.pi, 0.1)

    # Utilizar la función np.sin para someter cada valor de "X",
    # obtenga el array "y_nump" que tenga los resultados
    # NO utilizar comprensión de listas, solo utilice la
    # funcion de numpy "np.sin"

    y_nump = np.sin(x)
    #print(y_nump)

    # Conjunto de valores "X" en una lista
    x = list(np.arange(0, 2*np.pi, 0.1))

    # Utilizar comprensión de listas para obtener la lista
    # "y_list" que tenga todos los valores obtenidos como resultado
    # de someter cada valor de "X" a la función math.sin
    
    y_list = [math.sin(valor) for valor in x]
    print(y_list)

    # Este es un ejemplo práctico de cuando es útil usar numpy,
    # basicamente siempre que deseen utilizar una función matemática
    # que esté definida en numpy NO necesitaran un bucle o comprensión
    # de listas para obtener el resultado de un monton de datos a la vez.


def ej4():
    print("Acercamiento al uso de datos relacionales")
    # Transformar variable numéricas en categóricas
    # Se dispone del siguiente diccionario que traduce el número ID
    # de un producto en su nombre, por ejemplo:
    # NOTA: Esta información bien podría ser una tabla SQL: id | producto
    producto = {
                556070: 'Auto',
                704060: 'Moto',
                42135: 'Celular',
                1264: 'Bicicleta',
                905045: 'Computadora',
                }

    lista_compra_id = [556070, 905045, 42135, 5674, 704060, 1264, 42135, 3654]
       
    # Crear una nueva lista "lista_compra_productos" que transforme la lista
    # realizada por "ID" de producto en lista por "nombre" producto
    # Iterar sobre la lista "lista_compra_id" para generar la nueva
    # En cada iteración acceder al diccionario para traducir el ID.
    # NOTA: Tener en cuenta que puede haber códigos (IDs) que
    # no esten registrados en el sistema, en esos casos se debe
    # almacenar en la lista la palabra 'NaN', para ello puede hacer uso
    # de condicionales PERO recomendamos leer atentamente el método "get"
    # de diccionarios que tiene un parametro configurable respecto
    # que sucede sino encuentra la "key" en el diccionario.     

    lista_compra_productos = list(map(producto.get, lista_compra_id)) #SOLO ME DA LOS VALORES Y LOS QUE NO ESTAN EN EL DICT LO REEMPLAZA CON NONE
    
    lista_compra =  [x if x in producto else 'NaN' for x in lista_compra_id] #ESTA ME DA LAS CLAVES Y REEMPLAZA CON NAN LOS QUE NO ESTAN EN DICT

    lista_compra_productos1 = [producto.get(x, 'NaN') for x in lista_compra_id] #ESTA ES LA APROPIADA
    
    # Inove: Exacto! la ltima es la apropiada
    
    print(lista_compra_productos)
    print(lista_compra)
    print(lista_compra_productos1)
    
    
def evaluar(jugador, persona):
    
    if jugador == 0:
        pass
    
    else:
        if jugador >= 21:
            print(persona, 'superaste los 21 puntos con:', jugador, 'puntos')

        elif jugador < 21:
            print(persona, 'tiene acumulados', jugador, 'puntos')    
     

def ej5():
    print("Ahora sí! buena suerte :)")

    '''
    Black jack! [o algo parecido :)]

    El objetivo es realizar una aproximación al juego de black jack,
    el objetivo es generar una lista de 2 números aleatorios
    entre 1 al 10 inclusive, y mostrar los "números" al usuario.
    El usuario debe indicar al sistema si desea sacar más
    números para sumarlo a la lista o no sacar más
    A medida que el usuario vaya sacando números aleatorios que se suman
    a su lista se debe ir mostrando en pantalla la suma total
    de los números hasta el momento.
    Cuando el usuario no desee sacar más números o cuando el usuario
    haya superado los 21 (como la suma de todos) se termina la jugada
    y se presenta el resultado en pantalla

    BONUS Track: Realizar las modificaciones necesarias para que jueguen
    dos jugadores y compitan para ver quien sacá la suma de números
    más cercanos a 21 sin pasarse!
    '''
    contador = 0

    try:
        print('Bienvenido al juego Black Jack')
        print('Cuántos jugadores jugaran?')
        print('Ingrese 1, para un jugador:\n Ingrese 2, para dos jugadores:\n Ingrese 3, para salir')
        jugadores = int(input())
    
    except ValueError:
        print('El valor indicado no corresponde con lo indicado. Intente nuevamente.')
        print('Bienvenido al juego Black Jack')
        print('Cuántos jugadores jugaran?')
        print('Ingrese 1, para un jugador:\n Ingrese 2, para dos jugadores:\n Ingrese 3, para salir')
        jugadores = int(input())
    
    
    if jugadores == 1:
        
        try:
            print('Escriba "JUGAR", para sacar números:\n Ingrese "SALIR", para no sacar más números:')
            consulta = str(input())
        except:
            print('El valor indicado no corresponde con lo indicado. Intente nuevamente.')
            print('Escriba "JUGAR", para sacar números:\n Ingrese "SALIR", para no sacar más números:')
            consulta = str(input())
          
        while consulta:
            
            if consulta == 'JUGAR':   
                jugador1 = [random.randint(1, 11) for x in range(2)]
                suma1 = sum(jugador1)
                lista_jugador1.append(jugador1)             
                suma_jugador1.append(suma1)
                contador += 1
                                    
                print('Intento:', contador,'. Resultados:', jugador1)
                evaluar(jugador= sum(suma_jugador1), persona= 'jugador1')
                
                #--------------PARA SABER SI SUPERA LOS 21 PUNTOS Y TERMINA LA JUGADA--------                
                if sum(suma_jugador1) >= 21 or consulta == 'SALIR':
                    print('Termina la jugada')
                    print('Resultados en puntaje:', sum(suma_jugador1))
                    break
                
                try:
                    print('Escriba "JUGAR", para sacar números:\n Ingrese "SALIR", para no sacar más números:')
                    consulta = str(input())
                
                except:
                    print('El valor indicado no corresponde con lo indicado. Intente nuevamente.')
                    print('Escriba "JUGAR", para sacar números:\n Ingrese "SALIR", para no sacar más números:')
                    consulta = str(input())

            elif consulta == 'SALIR':
                break

            else:
                print('Los valores ingresados no corresponden, intente nuevamente')
                try:
                    print('Escriba "JUGAR", para sacar números:\n Ingrese "SALIR", para no sacar más números:')
                    consulta = str(input())
                except:
                    print('El valor indicado no corresponde con lo indicado. Intente nuevamente.')
                    print('Escriba "JUGAR", para sacar números:\n Ingrese "SALIR", para no sacar más números:')
                    consulta = str(input())

    elif jugadores == 2:
        print('Escriba "JUGAR", para sacar números:\n Ingrese "SALIR", para no sacar más números:')
        consulta = str(input())

        while consulta:
            
            if consulta == 'JUGAR':       
                jugador1 = [random.randint(1, 11) for x in range(2)]
                jugador2 = [random.randint(1, 11) for x in range(2)]
                lista_jugador1.append(jugador1)
                lista_jugador2.append(jugador2)
                suma1 = sum(jugador1) 
                suma2 = sum(jugador2)              
                suma_jugador1.append(suma1)              
                suma_jugador2.append(suma2)
                contador += 1

                print('Intento:', contador,'. Resultados:', jugador1)
                print('Intento:', contador,'. Resultados:', jugador2)                
                evaluar(jugador= sum(suma_jugador1), persona= 'jugador1')
                evaluar(jugador= sum(suma_jugador2), persona= 'jugador2')
                
                if sum(jugador1) == 0 and sum(suma_jugador2) == 0:
                    pass 
        
                elif sum(jugador1) == sum(suma_jugador2):
                    print('Quedaron con igual puntaje, jugador1', sum(suma_jugador1),'jugador2', sum(suma_jugador2))
                        
                #--------------PARA SABER SI SUPERA LOS 21 PUNTOS Y TERMINA LA JUGADA--------

                elif (sum(suma_jugador1) >= 21 and sum(suma_jugador1) > sum(suma_jugador2)) or consulta == 'SALIR':
                    print('Termina la jugada')
                    print('Gana la jugada el jugador1 con un puntaje total de:', sum(suma_jugador1), 'puntos de:', jugador1)
                    break

                elif (sum(suma_jugador2) >= 21 and sum(suma_jugador2) > sum(suma_jugador1)) or consulta == 'SALIR':
                    print('Termina la jugada')
                    print('Gana la jugada el jugador2 con un puntaje total de:', sum(suma_jugador2), 'puntos de:', jugador2)
                    break
                
                #--------------------PARA CONTINUAR EL JUEGO EN CASO NO HAYA SUPERADO LOS 21 PUNTOS-----

                print('Escriba "JUGAR", para sacar números y jugar otra vez:\n Escriba "SALIR", para no sacar más números:')
                consulta = str(input())

            elif consulta == 'SALIR':
                break

            else:
                print('Los valores ingresados no corresponden, intente nuevamente')
                print('Escriba "JUGAR", para sacar números y jugar otra vez:\n Escriba "SALIR", para no sacar más números:')
                consulta = str(input())
        
    elif jugadores == 3:
        print('Ha salido del programa')
    
    else:
        print('Los valores ingresados no corresponden con los indicados, intente nuevamente.')
        try:
            print('Cuántos jugadores jugaran?')
            print('Ingrese 1, para un jugador:\n Ingrese 2, para dos jugadores:\n Ingrese 3, para salir')
            jugadores = int(input())
        
        except ValueError:
            print('El valor indicado no corresponde con lo indicado. Intente nuevamente.')
            print('Cuántos jugadores jugaran?')
            print('Ingrese 1, para un jugador:\n Ingrese 2, para dos jugadores:\n Ingrese 3, para salir')
            jugadores = int(input())

                  
if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    #ej2()
    #ej3()
    ej4()
    # jugador = int()
    # lista_jugador = list()
    # persona = ''
    # evaluar(jugador, persona)
    # ej5()
    
