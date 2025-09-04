Este laboratorio presenta una implementación vulnerable de autenticación en dos pasos. Aunque disponemos del usuario y la contraseña de Carlos, no tenemos acceso al segundo factor: un código de 4 dígitos que cambia constantemente.

El problema de fondo es que, tras dos intentos fallidos del código 2FA, la sesión es invalidada. Para solventarlo, usamos Burp Suite y configuramos una Session Handling Rule que automatiza el login en cada intento.

Primero, grabamos un **macro** que simula el flujo completo: desde cargar el formulario de login, enviar las credenciales de Carlos y llegar a la pantalla de verificación. Este macro se ejecutará automáticamente antes de cada intento enviado por Intruder, permitiéndonos probar un código diferente sin que expire la sesión.

Este paso es fundamental para poder realizar un ataque por fuerza bruta de forma sostenida contra el 2FA.

Solucion
en esta ocacion si tenemos credenciales
![Pasted_image_20250820230521.png](/Imagenes/Pasted_image_20250820230521.png)
el problema se presenta cuando nos pide un codigo de 4 digitos
![Pasted_image_20250820230556.png](/Imagenes/Pasted_image_20250820230556.png)
el cual nosotros no tenemos
y esto lo vamos interceptando y viendo en http history
![Pasted_image_20250820230808.png](/Imagenes/Pasted_image_20250820230808.png)
el cual vamos a mandar al repeater
pero si lo volvemos a dar 2 veces podemos ver que en efecto ya no se emplea lo cual tendremos que repetir el mismo proceso de nuevo para seguir haciendo pruebas
![Pasted_image_20250820230932.png](/Imagenes/Pasted_image_20250820230932.png)entonces la idea seria automatizar las respestas que en este caso seria la del primer login, ya logeados, y el codigo de authenticacion 
esto lo requerimos para poder tomar el csrf que contiene
![Pasted_image_20250820231419.png](/Imagenes/Pasted_image_20250820231419.png)asi que esto lo vamos automatizar con BS le damos en settings le damos add le ponemos un nombre
![Pasted_image_20250820231624.png](/Imagenes/Pasted_image_20250820231624.png)
en la parte de Scope le ponemos todas las urls
![Pasted_image_20250820231732.png](/Imagenes/Pasted_image_20250820231732.png)
regresa,ps a details le damos add le de damos RUN a Macro una vez en la macro le damos add y se nos abren las solicitudes
![Pasted_image_20250820231855.png](/Imagenes/Pasted_image_20250820231855.png)
y seleccionamos las que mencionamos anteriormente
![Pasted_image_20250820232004.png](/Imagenes/Pasted_image_20250820232004.png)

