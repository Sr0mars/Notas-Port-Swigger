Aquí generamos una ‘cookie stay-logged-in’ válida para el usuario administrator utilizando el oracle de cifrado del parámetro **email**.

Para evitar el prefijo añadido, manipulamos el padding y truncamos los primeros 32 bytes del resultado desencriptado. Con la cookie final correctamente ajustada, accedemos al panel de administración y eliminamos al usuario carlos, resolviendo el laboratorio.

Solucion
Entonces nos copiamos la cadena del response
![Pasted_image_20250829013717.png](/Imagenes/Pasted_image_20250829013717.png)
entonces selecciona los 23 bytes
![Pasted_image_20250829013916.png](/Imagenes/Pasted_image_20250829013916.png)
los eliminamos
![Pasted_image_20250829014147.png](/Imagenes/Pasted_image_20250829014147.png)
y la cadena de hasta abajo la copiamos la urlcodeamos y la pegamos en el web
![Pasted_image_20250829014307.png](/Imagenes/Pasted_image_20250829014307.png)
esto significa que hay rellenar los bites que hemos eliminado
asi que vamos a gregar 9 bytes mas que se veran representados asi
![Pasted_image_20250829014900.png](/Imagenes/Pasted_image_20250829014900.png)
repetimos el proceso
![Pasted_image_20250829014931.png](/Imagenes/Pasted_image_20250829014931.png)
de tal manera que vamos a eliminar las primeras 2 filas
![Pasted_image_20250829015116.png](/Imagenes/Pasted_image_20250829015116.png)
y la nueva cadena 
![Pasted_image_20250829015202.png](/Imagenes/Pasted_image_20250829015202.png)
la copiamos y la urlcodeamos (IOhtQXxflWyvQBCzPxkwaymzoyqlDAb6%2btDAelLcbhg%3d) pegamos en la web en la cookie 
![Pasted_image_20250829015316.png](/Imagenes/Pasted_image_20250829015316.png)
por lo que ahora nos deslogeamos y en login pegamos esta cookie
![Pasted_image_20250829015558.png](/Imagenes/Pasted_image_20250829015558.png)
![Pasted_image_20250829015617.png](/Imagenes/Pasted_image_20250829015617.png)
y ya solo eliminamos el usuario carlos
![Pasted_image_20250829015641.png](/Imagenes/Pasted_image_20250829015641.png)

