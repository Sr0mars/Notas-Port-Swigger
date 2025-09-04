En este laboratorio, se explota una mala implementación del sistema de “Mantener la sesión iniciada”. La cookie utilizada para esta funcionalidad contiene el nombre de usuario y el hash MD5 de la contraseña, codificados en Base64. Esto permite construir manualmente cookies válidas si se conocen o se adivinan las credenciales del usuario.

Primero, se observa el formato de la cookie con una cuenta propia y se confirma que contiene el nombre de usuario seguido del hash MD5 de la contraseña. A partir de esta estructura, se puede automatizar la construcción de nuevas cookies usando una lista de contraseñas, aplicando los siguientes pasos: hashear cada contraseña con MD5, anteponer el nombre de usuario (Carlos), y codificar el resultado en Base64.

El ataque se lanza con Burp Intruder, configurando reglas de procesamiento de payloads y detectando el éxito de la intrusión al identificar elementos únicos de una sesión iniciada como “Update email” en la respuesta. Cuando esto ocurre, se confirma que la cookie generada pertenece a Carlos y se obtiene acceso a su cuenta.

Solucion
bueno hacemos el mismo procedimiento de siempre y como podemos ver en una de las peticiones vemos que tenemos un cadena en base64 que una vez la decodificamos vemos que se trata de la contraseña de peter
![Pasted_image_20250820210430.png](Imagenes/Pasted_image_20250820210430.png)
![Pasted_image_20250820210541.png](Imagenes/Pasted_image_20250820210541.png)
asi que esto lo vamos a mandar al intruder
ya estando en el intruder vamos a configurar en la parte de payload processing uno que sea (HASH, MD5)
![Pasted_image_20250820211213.png](Imagenes/Pasted_image_20250820211213.png)
otro que seria carlos:
![Pasted_image_20250820211349.png](Imagenes/Pasted_image_20250820211349.png)
y una configuracion por que necesita estar todo en base64
![Pasted_image_20250820211501.png](Imagenes/Pasted_image_20250820211501.png)
y le damos starattack
y bueno una ves termine vemos que tenemo una respuesta 200
![Pasted_image_20250820212340.png](Imagenes/Pasted_image_20250820212340.png)
y obtenemos la cookie en este caso en la RESPUESTA y aplicamos
![Pasted_image_20250820212507.png](Imagenes/Pasted_image_20250820212507.png)
