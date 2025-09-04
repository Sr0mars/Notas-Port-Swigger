En esta clase explotamos una vulnerabilidad de server-side prototype pollution en una aplicación Node.js que nos permite ejecutar comandos arbitrarios en el sistema. Usamos la funcionalidad de cambio de dirección para enviar un objeto JSON con la propiedad ‘**proto**‘, inyectando un campo ‘**execArgv**‘ que se utiliza en los procesos hijos del servidor.

Al manipular este campo con el argumento ‘**–eval**‘, forzamos al proceso a ejecutar código JavaScript, como una llamada a ‘**execSync**‘. Inicialmente probamos la ejecución contactando con Burp Collaborator mediante una petición **curl**, y al confirmarlo, sustituimos ese comando por otro que elimina el archivo ‘**/home/carlos/morale.txt**‘.

Esta clase demuestra cómo una simple entrada JSON puede comprometer por completo el sistema, combinando prototype pollution con ejecución de comandos a nivel de servidor.

Solucion
vamos a interceptar esto vemos que ya somos admin
![Pasted_image_20250901004554.png](/Imagenes/Pasted_image_20250901004554.png)
![Pasted_image_20250901004741.png](/Imagenes/Pasted_image_20250901004741.png)
si nos regresamos a la pagina y le damos click al admin panel nos sale esto y de igual forma vamos a interceptarlo
![Pasted_image_20250901004844.png](/Imagenes/Pasted_image_20250901004844.png)
![Pasted_image_20250901004941.png](/Imagenes/Pasted_image_20250901004941.png)
vamos a tratar de ver si es vulnerable a prototipe el profile de esta manera (,"__proto__":{"json spaces":10})
vemos que si
![Pasted_image_20250901005310.png](/Imagenes/Pasted_image_20250901005310.png)
y podemos meter una nuevo argumento
"__proto__": {"execArgv":["--eval=require('child_process').execSync('rm /home/carlos/morale.txt')"]}
¿Qué está intentando hacer?
• 	execArgv: es una propiedad que se usa en Node.js para pasar argumentos al proceso principal cuando se inicia.
• 	--eval: le dice a Node que ejecute el código que sigue directamente como si fuera un script.
• 	require('child_process').execSync(''): ejecuta un comando del sistema de forma síncrona.
• 	rm /home/carlos/morale.txt: intenta borrar el archivo  en la ruta especificada

![Pasted_image_20250901010218.png](/Imagenes/Pasted_image_20250901010218.png)
y su volvemos al admin panel y le damos al boton vemos que se a eliminando
![Pasted_image_20250901010322.png](/Imagenes/Pasted_image_20250901010322.png)

