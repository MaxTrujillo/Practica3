lista1 = [10,20,30]
lista2 = [40,50,60]
print(lista1 + lista2)


listaA = ['audi','toyota','mazda']
puerta = [2,4]
print("Mi auto es: " + listaA[-1].title())
print(f"Mi auto {listaA[-2].title()} tiene {puerta[-2]} puertas")

lista3 = [100,500,200,7000,-200,]
print(sum(lista3)) #Sumando cada elemento de una lista con la función "sum"
print(max(lista3)) #Máximos de los elemento de una lista con la función "max"
print(min(lista3)) #Mínimo de los elemento de una lista con la función "min"

lista1 = list(range(7)) #lista de 0 a 6 NO CONSIDERA 7
lista2 = list(range(1,10)) #lista de de 1 a 9 NO CONSIDERA 10
lista3 = list(range(-10,2)) #lista de 10 a 1 NO CONSIDERA 2
lista4 = list(range(200,100,-20)) #lista de 200 a 100 restando 20
lista5 = list(range(200,100,20)) #lista vacia rango inicia en 200 avanza sumando
print(lista1)
print(lista2)
print(lista3)
print(lista4)
print(lista5)

autos = ['mazda', 'audi', 'toyota', 'subaru', 'bmw', 'lamborghini']
print (autos[6].upper())

# Método 1: Utilizando if-elif-else
x = int(input("Ingrese un numero entero, positivo o negativo: "))

# Verificación de número positivo, negativo o cero
if x > 0:
    y = "positivo"
elif x < 0:
    y = "negativo"
else:
    y = "cero"

# Mostrar el resultado
print("\nEl numero: {}".format(x))
print("Es un numero: {}".format(y))

# Método 2: Utilizando elif

# ****** FUNCIÓN detecta POSITIVOS NEGATIVOS ******
def det(xx):
    if xx < 0:
        p = 'negativo'
    elif xx > 0:
        p = 'positivo'
    else:
        p = 'cero'
    
    print(p)  # Esto imprimirá el resultado
    return p  # Devolvemos el valor de p

### Ingresamos NUMERO ******************
num = int(input("Ingrese un numero entero, positivo o negativo: "))  # Ingresar número

### Llamamos A LA FUNCIÓN *****************
resp = det(num)  # Asignamos el valor devuelto por la función a 'resp'

# Imprimo RESULTADO
print("\nEl numero: {}".format(num))
print("Es un numero: {}".format(resp))

from math import pi

# Ingresar radio del círculo
radio = float(input("Ingrese el radio de un círculo: "))

# Menú
print("Seleccione una opción: ")
print("a) Calcular el diámetro.")
print("b) Calcular el perímetro.")
print("c) Calcular el área.")

# Selección de opción
opcion = input("Digita a, b, o c y presiona enter: ")

# Condicionales anidados (Mejorado)
if opcion == "a":
    diametro = 2 * radio
    print("\nEl diámetro del Círculo es: {0}".format(diametro))
elif opcion == "b":
    perimetro = 2 * pi * radio
    print("\nEl perímetro del Círculo es: {0}".format(perimetro))
elif opcion == "c":
    area = pi * radio ** 2
    print("\nEl área del Círculo es: {0}".format(area))
else:
    print("\nSolo hay tres opciones: a, b, c.")
    print(f'Tu has tecleado "{opcion}".')
    
from math import pi

# Ingresar radio del círculo
radio = float(input("Ingrese el radio de un círculo: "))

# Menú de opciones
print("Seleccione una opción: ")
print("a) Calcular el diámetro.")
print("b) Calcular el perímetro.")
print("c) Calcular el área.")

# Leer la opción seleccionada
opcion = input("Digita a, b, o c y presiona enter: ")

# Condicionales con elif
if opcion == "a":
    diametro = 2 * radio
    print("El diámetro del Círculo es: {0}".format(diametro))
elif opcion == "b":
    perimetro = 2 * pi * radio
    print("El perímetro del Círculo es: {0}".format(perimetro))
elif opcion == "c":
    area = pi * radio ** 2
    print("El área del Círculo es: {0}".format(area))
else:
    print("Solo hay tres opciones: a, b, c.")
    print(f'Tu has tecleado "{opcion}".')
    
alimento = ['arroz', 'papas', 'camotes', 'leche', 'carne', 'cebolla', 'tomate', 'lechuga']

if 'carne' in alimento:  # Condicional Si "carne" está en la lista de alimentos
    print('Hoy comemos rica Parrilla!!!!')
else:
    print('Hoy comemos Verduras')

# ******* FUNCION JUGERÍA ****************************************************
def preparar(fruit):
    if fruit in fruta:  # Verificamos si la fruta está en la lista
        print(f'\nSi tenemos {fruit.upper()} !!!, te prepararemos un Jugo')
    else:
        print(f'\nHoy no tenemos {fruit.upper()}, pero regresa Mañana')

# ******* Lista de Frutas ***************************************************
fruta = ['platano', 'manzana', 'pera', 'naranja', 'mandarina', 'uva']

antojo = input('Ingresa la fruta que deseas comer hoy : ')  # Pedimos la fruta al usuario
preparar(antojo)  # Llamamos a la función para verificar si tenemos la fruta
print('\nGracias por tu Preferencia !!!, Vuelve Pronto')

#************* FUNCIÓN que detecte la mayoría de edad ************
def mayoria(nom, xx):
    if xx >= 18:
        print(f'\n{nom.upper()} es Mayor de Edad con {xx} años de edad')
    else:
        print(f'\n{nom.upper()} es Menor de Edad con {xx} años de edad')

#************** INGRESA DATOS ************************************
nombre = input('Ingresa tu Nombre: ')
edad = int(input('Ingrese su edad: '))

mayoria(nombre, edad)  # Llamamos a la función para comprobar si es mayor o menor de edad
