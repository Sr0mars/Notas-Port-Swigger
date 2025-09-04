En esta clase vemos cómo una validación deficiente de direcciones de correo puede permitir acceso no autorizado. La aplicación restringe el acceso al panel de administración a usuarios con correos del dominio dontwannacry.com, pero recorta cualquier dirección a 255 caracteres sin volver a validar el dominio después del truncamiento.

Al registrar una cuenta con una dirección larga que contenga **@dontwannacry.com** justo antes del límite, logramos que el sistema guarde una dirección aparentemente legítima y nos dé acceso al panel de administración. Desde ahí, eliminamos al usuario carlos para completar el laboratorio.

Solucion
bueno nos dice que tenemos un panel de administracion pero cuando tratamos de entrar nos dice que no tenemos permiso
![Pasted_image_20250828222322.png](Imagenes/Pasted_image_20250828222322.png)
nos comparten un email client
![Pasted_image_20250828222453.png](Imagenes/Pasted_image_20250828222453.png)
por lo cual pasamos a registrarnos pero vamos a poner otro nombre en el correo
![Pasted_image_20250828222548.png](Imagenes/Pasted_image_20250828222548.png)
vemos que nos ha llegado un correo si le picamos al link se activara la cuenta
![Pasted_image_20250828222629.png](Imagenes/Pasted_image_20250828222629.png)
![Pasted_image_20250828222645.png](Imagenes/Pasted_image_20250828222645.png)
pero aun asi no podemos ingresar al panel admin por lo cual procedemos a crearnos otro usuario pero esta vez le vamos a cambiar
solo que en esta ocacion vamos agregar una cadena de A
![Pasted_image_20250828224306.png](Imagenes/Pasted_image_20250828224306.png)
tal que quede asi
![Pasted_image_20250828224333.png](Imagenes/Pasted_image_20250828224333.png)
de igual forma nos llegara un correo
![Pasted_image_20250828224417.png](Imagenes/Pasted_image_20250828224417.png)
tal que cuando nos volvamos a logear nos quedara asi entrando al panel admin
![Pasted_image_20250828224457.png](Imagenes/Pasted_image_20250828224457.png)
y ya solo eliminamos al usuario carlos
![Pasted_image_20250828224532.png](Imagenes/Pasted_image_20250828224532.png)
