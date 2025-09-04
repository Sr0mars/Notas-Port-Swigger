En esta clase exploramos cómo burlar los mecanismos de rate limiting explotando una condición de carrera durante el proceso de autenticación. Aunque el servidor bloquea el login tras varios intentos fallidos, descubrimos que al enviar múltiples peticiones en paralelo antes de que el contador de intentos se actualice, es posible colar más intentos de los permitidos.

Usamos **Turbo Intruder** en modo HTTP/2 para lanzar todos los intentos simultáneamente, evitando el bloqueo y encontrando la contraseña válida del usuario ‘**carlos**‘.

Esta técnica demuestra cómo pequeñas ventanas de tiempo pueden ser suficientes para ejecutar ataques efectivos contra sistemas mal implementados.

Solucion
nos comparten una lista de contraseñas
![Pasted_image_20250901183347.png](Imagenes/Pasted_image_20250901183347.png)
la contraseña que nos dan es la siguiente
wiener -peter
tenemos que forzar un error en el login para que nos salga este mensaje
![Pasted_image_20250901183523.png](Imagenes/Pasted_image_20250901183523.png)
esto se hace poniendo mal la contraseña de wiener probando con test u otra unas 3 veces aprox, esto lo mandamos al repeater
y realizamos un grupo
![Pasted_image_20250901183846.png](Imagenes/Pasted_image_20250901183846.png)
tal que la idea es realizar varias solicitudes pero con diferentes contraseñas
![Pasted_image_20250901183921.png](Imagenes/Pasted_image_20250901183921.png)
y con la extencion la turbo intruder seleccionamos la contraseña damos click derecho y send to turbo intruder
![Pasted_image_20250901184129.png](Imagenes/Pasted_image_20250901184129.png)
y vamos a seleccionar el siguiente payload
![Pasted_image_20250901184215.png](Imagenes/Pasted_image_20250901184215.png)
y lo modificamos tal que queda asi
nos copiamos en la clipboard la lista de contraseñas
![Pasted_image_20250901184825.png](Imagenes/Pasted_image_20250901184825.png)
e iniciamos el ataque
tal que al finalizar nos dara la unica contraseña con estado 302
![Pasted_image_20250901190713.png](Imagenes/Pasted_image_20250901190713.png)
y ya solo ingresamos al lab nos logeamos y eliminamos al usario carlos
![Pasted_image_20250901190750.png](Imagenes/Pasted_image_20250901190750.png)
importante antes de mandar el ataque se tiene que configurar en el repeater el usuario carlos
![Pasted_image_20250901190839.png](Imagenes/Pasted_image_20250901190839.png)

