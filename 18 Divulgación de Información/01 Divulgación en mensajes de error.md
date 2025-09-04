En esta clase accedemos a una de las páginas de producto y, mediante Burp Suite, interceptamos la petición que contiene el parámetro ‘**productId**‘. Al modificar su valor por un tipo de dato inesperado (por ejemplo, una cadena de texto), provocamos que la aplicación genere una excepción.

Esta excepción muestra una traza completa del error, lo que nos permite descubrir detalles técnicos sobre el sistema.

Solucion
La web:
![Pasted_image_20250827221017.png](/Imagenes/Pasted_image_20250827221017.png)
le damos algun producto
![Pasted_image_20250827221059.png](/Imagenes/Pasted_image_20250827221059.png)
y si en la url en ves de 2 ponemos test nos arroga un error que nos en lista la version
![Pasted_image_20250827221140.png](/Imagenes/Pasted_image_20250827221140.png)
copiamos la version y la ponemos en el laboratorio
![Pasted_image_20250827221226.png](/Imagenes/Pasted_image_20250827221226.png)
