En esta clase exploramos cómo una API controlada por un modelo de lenguaje permite interacciones peligrosas al no restringir adecuadamente los datos introducidos. Aprovechamos la funcionalidad de suscripción a un boletín para inyectar comandos del sistema utilizando la sintaxis ‘**$(…)**‘.

Verificamos primero que el comando se ejecuta usando ‘**whoami’**, y finalmente conseguimos borrar el archivo ‘**morale.txt**‘ ubicado en el directorio de Carlos. Este ejercicio demuestra cómo una exposición descuidada de APIs puede derivar en ejecución remota de comandos críticos.

Solucion
bueno entramos a la web y vemos que nuevamente tenemos acceso a un live chat
![Pasted_image_20250902113914.png](/Imagenes/Pasted_image_20250902113914.png)
vamos a pedirle mas informacion
![Pasted_image_20250902114359.png](/Imagenes/Pasted_image_20250902114359.png)
y bueno en subscribe_to_newsletter podemos pasarle nuestro emailclient
![Pasted_image_20250902114833.png](/Imagenes/Pasted_image_20250902114833.png)
vemos que nos ah registrado
![Pasted_image_20250902114853.png](/Imagenes/Pasted_image_20250902114853.png)
entonces algo que podemos hacer es injectar un comando a nivel de linux para ver si me da respuesta en este caso seria asi
![Pasted_image_20250902115224.png](/Imagenes/Pasted_image_20250902115224.png)
y si volvemos a recargar el correo
![Pasted_image_20250902115252.png](/Imagenes/Pasted_image_20250902115252.png)
vemos que somos carlos asi que lo que podemos hacer es eliminar el archivo
![Pasted_image_20250902115358.png](/Imagenes/Pasted_image_20250902115358.png)
por lo cual si vamos arriba vemos que el lab se ah resuelto
![Pasted_image_20250902115438.png](/Imagenes/Pasted_image_20250902115438.png)