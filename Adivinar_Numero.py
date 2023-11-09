import random

numero_aleatorio = random.randint(0, 99)

intentos = 0

while True:
    intento = int(input("Adivina el número: "))
    intentos += 1

    if intento == numero_aleatorio:
        print("¡Lo has adivinado!")
        print("Enhorabuena! Lo has conseguido adivinar en", intentos, "intentos!!")
        break
    
    elif intento > numero_aleatorio:
        print("Te has pasado, inténtalo otra vez.")

    elif intento < numero_aleatorio:
        print("Te has quedado corto, inténtalo otra vez.")