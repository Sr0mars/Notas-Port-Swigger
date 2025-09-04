Una vez preparado el entorno con Burp y automatizado el login mediante macros, procedemos a lanzar el ataque de fuerza bruta contra el parámetro mfa-code.

Usamos Burp Intruder con el tipo de payload Numbers, generando todos los códigos posibles del 0000 al 9999. También configuramos un resource pool con una sola solicitud concurrente, asegurando que no se envíen múltiples intentos en paralelo (lo que invalidaría la sesión).

Durante el ataque, eventualmente uno de los códigos es válido. Cuando eso ocurre, el servidor responde con un código 302, indicando redirección post-login exitoso.

Al identificar esta respuesta, cargamos dicha solicitud en el navegador y accedemos a la sección My account. De este modo, completamos el laboratorio demostrando que la implementación del segundo factor era vulnerable a fuerza bruta si no se aplicaban límites o protecciones adecuadas.

Solucion
si le damos a test macro podemos ver como se automatiza este procedimiendo que realizamos
![Pasted_image_20250820232240.png](/Imagenes/Pasted_image_20250820232240.png)
entonces le damos a todo OK
podemos ver que en session hemos creado una regla
![Pasted_image_20250820232356.png](/Imagenes/Pasted_image_20250820232356.png)
bueno una ves que lo tenemos ahora vamos a interceptar esto
![Pasted_image_20250820232553.png](/Imagenes/Pasted_image_20250820232553.png)
y lo mandamos al intruder
![Pasted_image_20250820232855.png](/Imagenes/Pasted_image_20250820232855.png)
lo modificamos de esta manera
![Pasted_image_20250820233051.png](/Imagenes/Pasted_image_20250820233051.png)
y le damos start attack
y tenemos que esperar bastante para poder ver es codigo de estado de error 302 para asi obtener la cookie y pegarla
![Pasted_image_20250820233331.png](/Imagenes/Pasted_image_20250820233331.png)
