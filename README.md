# Adivina el Número

## Primer Juego de Python

Puedes ver este repositorio en linea en el siguiente enlace: https://github.com/pablomarquezuax/Marquez_Pablo_PJ.git 

**Instrucciones de la tarea:** Va a crear un programa para terminal que va a escoger un número aleatoriamente, entre 0 y 99, y a continuación, le va a pedir al usuario que adivine este número.

Tras cada intento, le responderá indicándole si se ha quedado corto o se ha pasado, hasta que encuentre el número. Entonces, mostrará el número de intentos que han hecho falta para encontrar este número y el programa se terminará.

**Intrucciones para terminar el juego:**

- ***Paso 1:***

El primer cambio consiste en crear un menú que permita seleccionar un nivel de dificultad: nivel simple (entre 0 y 100), nivel intermedio (entre 0 y 1.000), nivel avanzado (entre 0 y 1.000.000) y nivel experto (entre 0 y 1.000.000.000.000).

El jugador podrá escoger de manera sencilla su nivel, por ejemplo entre 1 y 4, y los valores mínimo y máximo se determinarán automáticamente.

De manera opcional puede, sea cual sea el nivel, proponer al jugador una ayuda (mostrar el número mínimo y máximo deducidos de las anteriores entradas) o rechazarla.

Puede crear una función para gestionar este menú, que incluirá en un nuevo módulo entrada.menu. También debe crear nuevas funciones en el módulo juego y revisar la función jugar.


- ***Paso 2:***

De manera opcional puede, sea cual sea el nivel, proponer al jugador una ayuda (mostrar el número mínimo y máximo deducidos de las anteriores entradas) o rechazarla.

Puede crear una función para gestionar este menú, que incluirá en un nuevo módulo entrada.menu. También debe crear nuevas funciones en el módulo juego y revisar la función jugar.


- ***Paso 3:***

Al final de una partida ganada, puede también pedir al jugador su nombre y guardarlo en la tabla de mejores puntuaciones. En primer lugar, esta tabla se creará al inicio del programa y los datos se perderán una vez se cierre.