# Función para verificar el desayuno según las compras y el día
def verificar_desayuno(compras, dia):
    if dia == "Lunes":
        if "manzanas" in compras or "peras" in compras:
            return "Puedes desayunar jugo de manzanas o peras."
    elif dia == "Martes":
        if "platano" in compras and "fresa" in compras and "leche" in compras:
            return "Puedes desayunar jugo de leche con plátano y fresa."
    elif dia == "Miércoles":
        if "yogurt" in compras and "cereales" in compras:
            return "Puedes desayunar yogurt con cereales."
    elif dia in ["Jueves", "Viernes", "Sábado", "Domingo"]:
        if "papaya" in compras:
            return "Puedes desayunar papaya."
    return "No hay ingredientes para el desayuno."

# Lista de compras y día
compras = ["manzanas", "leche", "platano"]
dia = "Lunes"
print(verificar_desayuno(compras, dia))

import statistics

# Función para calcular estadísticas
def calcular_estadisticas(numeros):
    media = statistics.mean(numeros)
    mediana = statistics.median(numeros)
    frecuencia = {num: numeros.count(num) for num in set(numeros)}
    return media, mediana, frecuencia

# Ingresar los 20 números
numeros = [int(input(f"Ingrese el número {i+1}: ")) for i in range(20)]
media, mediana, frecuencia = calcular_estadisticas(numeros)

# Mostrar resultados
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Frecuencia: {frecuencia}")

# Función para ordenar lista
def ordenar_lista(objetos, orden="ascendente"):
    if orden == "ascendente":
        return sorted(objetos)
    elif orden == "descendente":
        return sorted(objetos, reverse=True)

# Ingresar los 10 objetos
objetos = [input(f"Ingrese el objeto {i+1}: ") for i in range(10)]

# Mostrar menú
opcion = input("¿Cómo quieres ordenar la lista? (ascendente/descendente): ").lower()
objetos_ordenados = ordenar_lista(objetos, opcion)

# Mostrar la lista ordenada
print("Lista ordenada:", objetos_ordenados)

# Listas de usuarios y contraseñas
nombres = ["juan", "ana", "pedro", "maria"]
contrasenas = ["1234", "5678", "abcd", "efgh"]

# Función de verificación
def verificar_usuario(nombre, contrasena):
    if nombre in nombres and contrasena in contrasenas:
        return f"Bienvenido {nombre.capitalize()}, eres un trabajador de MicroSecret."
    else:
        return "Acceso rechazado."

# Ingresar nombre y contraseña
nombre = input("Ingrese su nombre: ").lower()
contrasena = input("Ingrese su contraseña: ")

# Verificar acceso
print(verificar_usuario(nombre, contrasena))

# Función para verificar materiales
def verificar_materiales(materiales):
    if "clavos" in materiales and "madera" in materiales:
        return "Puedes construir una ventana."
    elif "plancha metal" in materiales and "soldadura" in materiales:
        return "Puedes construir una puerta metálica."
    elif "plancha de madera" in materiales and "madera" in materiales:
        return "Puedes construir una puerta."
    else:
        return "Debe comprar más materiales."

# Lista de materiales
materiales = ["clavos", "madera", "plancha metal"]
print(verificar_materiales(materiales))

# Función de selección
def seleccion_marina(sexo, edad, altura, peso, prueba):
    if edad >= 18:
        if sexo == "mujer" and altura >= 1.60 and 55 <= peso <= 60 and prueba > 65:
            return "Seleccionada para la Marina"
        elif sexo == "varon" and altura >= 1.65 and 55 <= peso <= 60 and prueba > 65:
            return "Seleccionado para la Marina"
    return "NO SELECCIONADO"

# Ingresar datos del postulante
sexo = input("¿Eres mujer o varón? ").lower()
edad = int(input("Ingrese su edad: "))
altura = float(input("Ingrese su altura (en metros): "))
peso = float(input("Ingrese su peso (en kg): "))
prueba = int(input("Ingrese los puntos obtenidos en la prueba: "))

# Verificar selección
print(seleccion_marina(sexo, edad, altura, peso, prueba))

# Función de verificación para TUC
def verificar_tuc(sexo, edad, examen_medico, examen_conocimiento, examen_manejo, pago):
    if edad >= 18 and examen_medico and examen_conocimiento > 80 and examen_manejo > 95 and pago == 10:
        return "APTO TUC"
    return "NO APTO TUC"

# Ingresar datos
sexo = input("¿Eres mujer o varón? ").lower()
edad = int(input("Ingrese su edad: "))
examen_medico = input("¿Aprobó el examen médico? (sí/no): ").lower() == "sí"
examen_conocimiento = int(input("Ingrese los puntos en el examen de conocimiento: "))
examen_manejo = int(input("Ingrese los puntos en el examen de manejo: "))
pago = float(input("Ingrese el monto pagado (10 soles): "))

# Verificar elegibilidad
print(verificar_tuc(sexo, edad, examen_medico, examen_conocimiento, examen_manejo, pago))