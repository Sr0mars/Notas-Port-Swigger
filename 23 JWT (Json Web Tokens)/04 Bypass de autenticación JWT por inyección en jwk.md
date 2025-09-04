En esta clase abordamos una vulnerabilidad en la verificación de JWTs relacionada con el uso del parámetro **jwk** en el encabezado del token. El servidor permite que el propio JWT contenga la clave pública con la que será validado, pero no comprueba si dicha clave proviene de una fuente confiable.

Aprovechamos esta debilidad generando un par de claves RSA y firmando un token falso que suplantará al usuario administrador. Al incluir nuestra clave pública dentro del **jwk** del encabezado, el servidor valida la firma sin cuestionar su origen, otorgándonos acceso al panel de administración. Desde ahí, eliminamos al usuario Carlos.

Esta técnica ilustra los peligros de confiar ciegamente en datos controlados por el cliente en mecanismos de autenticación.

Solucion
no logeamos verificamos si tenemos acceso al admin
![Pasted_image_20250830235358.png](Imagenes/Pasted_image_20250830235358.png)
vemos que no podemos interceptamos esto
nos vamos a la pestaña del JWT para ver si es asimetrico
![Pasted_image_20250830235500.png](Imagenes/Pasted_image_20250830235500.png)
vemos que si por el RS256
entonces ahora nos vamos ala extencion de JWT le damos a new RSA key le damos generate y le damos ok
![Pasted_image_20250830235733.png](Imagenes/Pasted_image_20250830235733.png)
ahora nos regresamos otra vez al intercep le damos attack y en Embedded JWK
![Pasted_image_20250830235856.png](Imagenes/Pasted_image_20250830235856.png)
![Pasted_image_20250831000025.png](Imagenes/Pasted_image_20250831000025.png)
le damos ok y vemos que se an agregado mas cosas en la cabecera
![Pasted_image_20250831000045.png](Imagenes/Pasted_image_20250831000045.png)
y ahora nos copiamos la cookie
la pegamos en la cookie de la pagina
![Pasted_image_20250831000246.png](Imagenes/Pasted_image_20250831000246.png)
