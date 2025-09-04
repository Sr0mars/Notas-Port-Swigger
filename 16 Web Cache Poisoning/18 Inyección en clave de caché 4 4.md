En la última etapa del ataque, se utiliza la cabecera ‘**Pragma: x-get-cache-key**‘ para manipular directamente cómo se forma la clave de caché en el servidor. Esto permite cachear versiones maliciosas de recursos como ‘**localize.js**‘ y hacer que todos los usuarios, incluida la víctima, los carguen automáticamente.

Se combinan la URL con el parámetro ‘**utm_content**‘, la inyección en **Origin**, la contaminación de parámetros, y el envenenamiento de caché para que al visitar ‘**/login?lang=en**‘, la víctima cargue una versión manipulada del script y el código malicioso se ejecute en su navegador, resolviendo el laboratorio.

Solucion
entonce revisando el codigo solamente tenemos que spamear las 2 consultas
tal que al final quedaria asi
Login
![Pasted_image_20250822204528.png](/Imagenes/Pasted_image_20250822204528.png)
localize
![Pasted_image_20250822204552.png](/Imagenes/Pasted_image_20250822204552.png)
y en la pagina recargamos
![Pasted_image_20250822204724.png](/Imagenes/Pasted_image_20250822204724.png)
