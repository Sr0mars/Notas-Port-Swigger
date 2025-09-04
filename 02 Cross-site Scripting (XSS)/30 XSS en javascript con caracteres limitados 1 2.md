En esta clase de nivel experto nos enfrentamos a un entorno donde la inyección se produce dentro de una URL con esquema JavaScript, pero con múltiples restricciones: algunos caracteres están bloqueados y no se permite el uso directo de espacios. A pesar de que puede parecer un desafío simple, la protección activa complica la ejecución directa del código.

Para resolverlo, utilizamos una estructura avanzada basada en funciones flecha y manejo de errores. Creamos un bloque con una función que lanza una excepción. Luego, asignamos la función de alerta al manejador onerror, lo que nos permite ejecutarla indirectamente. Usamos una conversión de objeto a cadena para activar la ejecución, evitando el uso de paréntesis o llamadas explícitas a funciones.

Además, insertamos el número 1337 dentro del contenido de la alerta como requiere el laboratorio. El exploit se dispara solo cuando se hace clic en el botón que redirige al blog, lo que simula un comportamiento realista donde el usuario completa la acción que activa el código.

Este laboratorio muestra cómo, incluso con múltiples capas de restricción, es posible ejecutar código si se comprende a fondo el comportamiento del motor de JavaScript y se combinan constructores de lenguaje de forma creativa.

Solucion
Lo primero en esta ocacion seria checar el codigo fuente en el apartado de comentarios
vemos una etiqueta href
![Pasted image 20250718175710.png](imagenes/Pasted image 20250718175710.png)
vamos a urlcondearlo
![Pasted image 20250718175813.png](imagenes/Pasted image 20250718175813.png)
obtenemos una direccion y un id
![Pasted image 20250718175929.png](imagenes/Pasted image 20250718175929.png)
esto que nos dice que ne back to blog existe una ruta que esta en analitycs lo vemos con Ctrl+shoft+c en red
![Pasted image 20250718180506.png](imagenes/Pasted image 20250718180506.png)
para verlo mejor en BS
pero lo importante que en la injeccion se le puede meter mas parametro cerrando las comillas y agragando una llave
Entonces lo primero seria identificar que tenemos en post = id
entonces podemos utilizar fuzz para ver que existe algun parametro si no es de esta forma no puede funcionar
/post?postId=1
wfuzz -c -w /usr/share/SecLists/Fuzzing/special-chars.txt 'https://0a9c00890352857d821bec9b009c00dc.web-security-academy.net/post?postId=2FUZZ%27},{x:%27'

![Pasted image 20250718183148.png](imagenes/Pasted image 20250718183148.png)
aqui podemos ver que obtenemos 2 caracteres especiales lo cual es una buena forma en este caso el que funciono fue el de &
por lo cual si ponemos el puntero en el back podemos ver esto
![Pasted image 20250718183535.png](imagenes/Pasted image 20250718183535.png)
