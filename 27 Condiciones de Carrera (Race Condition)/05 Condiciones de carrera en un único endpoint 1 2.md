Esta clase se centra en explotar una vulnerabilidad de tipo race condition donde un único endpoint permite modificar el email de una cuenta de usuario sin validación adecuada. Al enviar múltiples solicitudes simultáneas, provocamos una desincronización entre el momento en que el servidor almacena el nuevo correo pendiente y cuando genera el enlace de confirmación.

Esto nos permite forzar que dicho enlace se genere con una dirección de correo distinta a la que recibe el mensaje, facilitando así que el usuario reclame una dirección como **carlos@ginandjuice.shop** y obtenga privilegios de administrador.

El laboratorio demuestra cómo, incluso en flujos simples, los accesos paralelos mal gestionados pueden derivar en escaladas de privilegios críticas.

Solucion
lo primero nos logeamos vemos que tenemeos un email client
![Pasted_image_20250901201815.png](Imagenes/Pasted_image_20250901201815.png)
si cambiamos de correo test y le damos al boton
![Pasted_image_20250901201847.png](Imagenes/Pasted_image_20250901201847.png)
y abrimos el email podemos ver que nos a llegado una confirmacion
![Pasted_image_20250901201945.png](Imagenes/Pasted_image_20250901201945.png)
si vemos el historico vemos una solicitud por post que es la de change email la vamos a mandar al repeater
![Pasted_image_20250901202016.png](Imagenes/Pasted_image_20250901202016.png)
y vamos a crear un grupo y vamos a duplicar hasta 20 tabs y lo vamos a enviar en secuencia por separado
y vamos a cambiar cada una por test1,test2, y asi en la parte del correo para ver el comportamiento
![Pasted_image_20250901202313.png](Imagenes/Pasted_image_20250901202313.png)
![Pasted_image_20250901202339.png](Imagenes/Pasted_image_20250901202339.png)y lo volvemos a mandar en paralelo y vemos el comportamiento del email client
![Pasted_image_20250901202423.png](Imagenes/Pasted_image_20250901202423.png)se han desincronizados