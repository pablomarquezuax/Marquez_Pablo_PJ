import random

#Abrir el diccionario para guargar los nombres de los jugadores y sus puntuaciones (numero de intentos)
MEJORES_PUNTUACIONES = {}

#Esta función carga las mejores puntuaciones ya guardadas o crea un diccionario nuevo si no hay registros.
def cargar_mejores_puntuaciones():
    return {}

# Esta función muestra un menú de niveles para que elija uno. 
# Devuelve el rango del nivel seleccionado y un booleano que indica si se debe ofrecer ayuda durante el juego.
def seleccionar_nivel():
    print("Selecciona un nivel de dificultad:")
    print("1. Nivel Simple (0-100)")
    print("2. Nivel Intermedio (0-1,000)")
    print("3. Nivel Avanzado (0-1,000,000)")
    print("4. Nivel Experto (0-1,000,000,000,000)")

    opcion = int(input("Ingresa el número del nivel que prefieres: "))

    if opcion == 1:
        return 0, 100, True
    elif opcion == 2:
        return 0, 1000, True
    elif opcion == 3:
        return 0, 1000000, True
    elif opcion == 4:
        return 0, 1000000000000, True
    else:
        print("La opción que has seleccionado no es válida. Estás jugando en Nivel Simple por defecto.")
        return 0, 100, True

# Genera un número secreto aleatorio dentro del rango especificado.
def generar_numero_secreto(minimo, maximo):
    return random.randint(minimo, maximo)


# Muestra el rango actual del número secreto si el usuario ha solicitado ayuda.
# Si el input es cualquier cosa que no sea ¨si¨, el programa entiende que el jugador no necesita ayuda.
def ofrecer_ayuda(minimo, maximo):
    ayuda = input("¿Quieres recibir ayuda? (si/no): ")
    if ayuda == "si":
        print(f"Número mínimo: {minimo}, Número máximo: {maximo}")


# Muestra las mejores puntuaciones almacenadas hasta el momento.
def mostrar_mejores_puntuaciones():
    print("Mejores Puntuaciones:")
    for nombre, intentos in MEJORES_PUNTUACIONES.items():
        print(f"{nombre}: {intentos} intentos")


# Compara el número adivinado con el número secreto. 
# Devuelve un string que indica si el número es demasiado bajo, alto o correcto. 
# (Ese string luego se inserta en la respuesta del programa al jugador.)
def comparar_numeros(numero, secreto):
    if numero < secreto:
        return "bajo"
    elif numero > secreto:
        return "alto"
    else:
        return "correcto"


# La función principal del juego. 
# Inicia el juego 
# Solicita al usuario que elija un nivel 
# Genera un número secreto y maneja el juego hasta que el usuario adivina el número.
def jugar():
    minimo, maximo, ayuda = seleccionar_nivel()
    numero_secreto = generar_numero_secreto(minimo, maximo)
    intentos = 0

    print(f"¡Bienvenido al juego de adivinar el número! Nivel: {minimo}-{maximo}")

    while True:
        if ayuda:
            ofrecer_ayuda(minimo, maximo)

        intento = int(input("Adivina el número: "))
        intentos += 1

        resultado = comparar_numeros(intento, numero_secreto)
        print(f"Tu intento {intento} es {resultado}. Inténtalo de nuevo!")

        if resultado == "correcto":
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            nombre_jugador = input("Ingresa tu nombre para guardar tu puntuación: ")
            MEJORES_PUNTUACIONES[nombre_jugador] = intentos
            break

    mostrar_mejores_puntuaciones()


# Ejecuta automaticamente la función de ¨jugar()¨, así como el diccionario de mejores puntuaciones.
# Se utiliza para determinar si el script de Python se está ejecutando como un programa principal o si se está importando como un módulo en otro script.
# En este caso, se trata del programa principal y no de un módulo del mismo.
if __name__ == "__main__":
    MEJORES_PUNTUACIONES = cargar_mejores_puntuaciones()
    jugar()