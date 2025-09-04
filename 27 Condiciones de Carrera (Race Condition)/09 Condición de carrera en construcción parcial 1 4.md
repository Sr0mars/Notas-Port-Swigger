En esta clase analizamos en detalle el flujo de registro de usuarios, enfocados en la validación de tokens de confirmación. Aunque no tenemos acceso a correos del dominio requerido, descubrimos mediante la lectura del JavaScript que el endpoint final para confirmar el registro es **/confirm** con un parámetro **token**.

Al enviar valores atípicos como arrays vacíos en este parámetro, identificamos respuestas inesperadas que sugieren un breve estado inválido o incompleto en la base de datos.

Esto nos hace sospechar de una condición de carrera en la que la verificación puede completarse antes de que el token se registre correctamente.

Importante leer: https://portswigger.net/web-security/race-conditions#partial-construction-race-conditions

Solucion
![Pasted_image_20250901213119.png](Imagenes/Pasted_image_20250901213119.png)
aqui no nos comparten ningun usuario por lo que si nosotros nos vamos al registrer podemos ver que nos obligan a registrarnos con su dominio
![Pasted_image_20250901213457.png](Imagenes/Pasted_image_20250901213457.png)
el problema es que nosotros no contamos con ningun correo del dominio que nos piden aunque tenemos un email client no es la misma direccion esto lo vamos a mandar al repeater una vez que le demos al boton
entonces lo que nos queda es navegar en la web 
y cuando navegamos vemos un recurso
![Pasted_image_20250901213908.png](Imagenes/Pasted_image_20250901213908.png)
vemos que se trata de un tipo formulario de registro
![Pasted_image_20250901213952.png](Imagenes/Pasted_image_20250901213952.png)
mas abajo del codigo vemos que se emplea una validacion de token
![Pasted_image_20250901214125.png](Imagenes/Pasted_image_20250901214125.png)
vemos que arriba se emplea otro apartado de register ese lo mandamos al repeater
![Pasted_image_20250901214400.png](Imagenes/Pasted_image_20250901214400.png)
y este lo vamos a cambiar de metodo a post
![Pasted_image_20250901214714.png](Imagenes/Pasted_image_20250901214714.png)

