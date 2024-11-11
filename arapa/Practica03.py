
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 22:22:14 2024
@author: kevinarapa
"""

# Desarrollo
"""
En esta sección se desarrollan los conceptos básicos de listas y estructuras condicionales en Python.
"""

# Ejemplo de lista
mi_lista = [1, 2, 3, "hola"]
print("Lista original:", mi_lista)

# Acceder al primer y último elemento
print("Primer elemento:", mi_lista[0])
print("Último elemento:", mi_lista[-1])

# Modificar un elemento
mi_lista[3] = "mundo"
print("Lista modificada:", mi_lista)

# Estructura condicional para verificar si un número es positivo, negativo o cero
x = int(input("Ingrese un número para verificar: "))
if x > 0:
    print("El número es positivo")
elif x < 0:
    print("El número es negativo")
else:
    print("El número es cero")

# Ejemplos
"""
Aquí se presentan ejemplos de operaciones en listas y estructuras condicionales en Python.
"""

# Operaciones con listas
numeros = [10, 20, 30, 40, 50]

# Agregar un elemento
numeros.append(60)
print("Lista después de agregar un elemento:", numeros)

# Eliminar un elemento
numeros.remove(30)
print("Lista después de eliminar un elemento:", numeros)

# Ordenar la lista
numeros.sort()
print("Lista ordenada:", numeros)

# Verificar si un número es par o impar
n = int(input("Ingrese un número para verificar paridad: "))
if n % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")

# Ejercicios
"""
Ejercicio 1: Programa que verifica si un número es positivo, negativo o cero.
Ejercicio 2: Programa que calcula el diámetro, perímetro o área de un círculo.
"""

# Ejercicio 1
def verificar_numero():
    x = int(input("Ingrese un número: "))
    if x > 0:
        print("Es positivo")
    elif x < 0:
        print("Es negativo")
    else:
        print("Es cero")

verificar_numero()

# Ejercicio 2
from math import pi

def calcular_circulo():
    radio = float(input("Ingrese el radio del círculo: "))
    print("Seleccione una opción:")
    print("a) Calcular el diámetro")
    print("b) Calcular el perímetro")
    print("c) Calcular el área")
    
    opcion = input("Elija una opción (a, b, o c): ")
    if opcion == "a":
        print("El diámetro es:", 2 * radio)
    elif opcion == "b":
        print("El perímetro es:", 2 * pi * radio)
    elif opcion == "c":
        print("El área es:", pi * radio ** 2)
    else:
        print("Opción no válida.")

calcular_circulo()

