En esta clase abordamos cómo un control de seguridad mal implementado puede permitir a un atacante acceder a funciones reservadas para empleados.

Aunque el panel de administración está limitado a usuarios con email corporativo, al registrarnos con un correo legítimo y luego modificarlo por uno con dominio **@dontwannacry.com**, se nos concede acceso sin validar adecuadamente esta modificación. Esta incoherencia en la lógica nos permite entrar al panel de admin y eliminar al usuario carlos para resolver el laboratorio.

Solucion
si nosotros tratamos acceder al admin nos sale este error tenemos tambien una seccion de correo 
![Pasted_image_20250827233259.png](/Imagenes/Pasted_image_20250827233259.png)
pero antes vamos a registrarnos nos pide que si somos de la empresa nos registremos con ese dominio
![Pasted_image_20250827233429.png](/Imagenes/Pasted_image_20250827233429.png)
pero no nos sale nada si embargo en el la seccion de email nos dan un correo
![Pasted_image_20250827233609.png](/Imagenes/Pasted_image_20250827233609.png)
![Pasted_image_20250827233638.png](/Imagenes/Pasted_image_20250827233638.png)
y si nos llega un correo
![Pasted_image_20250827233729.png](/Imagenes/Pasted_image_20250827233729.png)
el cual cuando le picamos al link nos activa la cuenta
por lo cual nos logeamos
![Pasted_image_20250827234010.png](/Imagenes/Pasted_image_20250827234010.png)
una vez aqui podemos cambiar nuestro correo
![Pasted_image_20250827234053.png](/Imagenes/Pasted_image_20250827234053.png)
![Pasted_image_20250827234200.png](/Imagenes/Pasted_image_20250827234200.png)
ya solo nos vamos al admin y eliminamos a carlos
![Pasted_image_20250827234220.png](/Imagenes/Pasted_image_20250827234220.png)