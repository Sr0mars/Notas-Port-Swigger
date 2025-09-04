Este laboratorio presenta una vulnerabilidad lógica en el sistema de autenticación que permite evadir las protecciones contra ataques de fuerza bruta.

El punto clave está en que el servidor acepta el parámetro ‘**password**‘ en formato JSON como si fuera un array. Esto permite enviar una lista de posibles contraseñas en una sola solicitud, y si alguna de ellas es correcta, el servidor inicia sesión exitosamente.

Al modificar el cuerpo del request para que el campo ‘**password**‘ contenga un array con todos los candidatos de la lista, evitamos las restricciones habituales de protección por IP o por número de intentos. Esta técnica permite realizar un ataque de fuerza bruta completo en un único envío.

Tras recibir una respuesta con redirección (302), accedemos al navegador desde Burp con la sesión ya autenticada como Carlos y simplemente visitamos la sección My account para completar el laboratorio.

Solucion
em este caso vamos a interceptar el login
![Pasted_image_20250820225400.png](/Imagenes/Pasted_image_20250820225400.png)
entonce la idea aqui es poner todo el diccionario en la parte de password
![Pasted_image_20250820225852.png](/Imagenes/Pasted_image_20250820225852.png)
![Pasted_image_20250820230001.png](/Imagenes/Pasted_image_20250820230001.png)
ya solo copiamos la cookie y la pegamos
![Pasted_image_20250820230051.png](/Imagenes/Pasted_image_20250820230051.png)
