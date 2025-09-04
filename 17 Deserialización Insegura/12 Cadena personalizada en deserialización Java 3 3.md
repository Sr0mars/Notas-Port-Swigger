Una vez identificado el campo vulnerable y el número de columnas en la tabla, lanzamos una inyección UNION que fuerza una conversión errónea del campo password, provocando que aparezca en el mensaje de error.

Extraemos la contraseña del usuario administrador, iniciamos sesión con ella y accedemos al panel de administración. Finalmente, eliminamos al usuario Carlos para completar el laboratorio.

Solucion
despues de estar testienando los campos encontramos que nos daba un error por que esperaba un campo numerico y nosotros le metimos una cade de tipo string asi que lo convertimos en numerico y probamos
![Pasted_image_20250827011623.png](Imagenes/Pasted_image_20250827011623.png)
![Pasted_image_20250827011656.png](Imagenes/Pasted_image_20250827011656.png)
asi que vamos probando
![Pasted_image_20250827011855.png](Imagenes/Pasted_image_20250827011855.png)
![Pasted_image_20250827011913.png](Imagenes/Pasted_image_20250827011913.png)
![Pasted_image_20250827011953.png](Imagenes/Pasted_image_20250827011953.png)
![Pasted_image_20250827012017.png](Imagenes/Pasted_image_20250827012017.png)
![Pasted_image_20250827012135.png](Imagenes/Pasted_image_20250827012135.png)
union select NULL,NULL,NULL,cast(string_agg(username||':'||password, ',') as numeric),NULL,NULL,NULL,NULL from users
![Pasted_image_20250827012510.png](Imagenes/Pasted_image_20250827012510.png)
nos logeamos como admin y eliminamos al usuario carlos
![Pasted_image_20250827012623.png](Imagenes/Pasted_image_20250827012623.png)
![Pasted_image_20250827012644.png](Imagenes/Pasted_image_20250827012644.png)
