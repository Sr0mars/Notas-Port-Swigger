En esta clase se explora un ataque avanzado de password reset poisoning mediante la técnica de dangling markup, que aprovecha cómo se renderizan los correos en su formato HTML crudo.

El laboratorio parte del hecho de que al solicitar un reseteo de contraseña, el nuevo password no se entrega mediante un enlace con token, sino que es enviado directamente en el cuerpo del correo. Este contenido es renderizado de forma segura usando **DOMPurify**, pero la versión “raw” del correo en HTML no pasa por ningún tipo de sanitización, lo que abre la puerta al ataque.

El atacante manipula la cabecera Host en la solicitud POST de recuperación de contraseña, agregando una cadena especialmente construida que introduce una etiqueta HTML sin cerrar (a href=**…). Esto provoca que el navegador del destinatario —en este caso, el visor de correo del laboratorio— intente completar el HTML truncado enviando el resto de la información (incluyendo la nueva contraseña generada) como parte de una solicitud al servidor del atacante (exploit server).

En concreto, se rompe la estructura del href con un puerto falso o un carácter especial, y luego se inyecta una dirección apuntando al exploit server. Como resultado, el contenido que debería quedar en el cuerpo del correo (incluyendo la contraseña de Carlos) se convierte en parte de la URL de la solicitud enviada al servidor del atacante.

Finalmente, el atacante accede al exploit server, revisa los registros, recupera la nueva contraseña de Carlos y accede con sus credenciales.

Esta clase muestra cómo errores sutiles en el manejo del HTML en correos electrónicos pueden derivar en vulnerabilidades críticas que permiten secuestrar cuentas incluso sin necesidad de XSS ni interacción directa del usuario objetivo.

Solucion

nos comparten un exploit server en la web
![Pasted_image_20250829221022.png](/Imagenes/Pasted_image_20250829221022.png)
vamos acceder al login y ya estando en el login vamos a dar forget password
![Pasted_image_20250829221342.png](/Imagenes/Pasted_image_20250829221342.png)
aqui vamos a introducir el usuario wiener
![Pasted_image_20250829221410.png](/Imagenes/Pasted_image_20250829221410.png)
y vemos en el email nos llega una estructura un poco diferente
![Pasted_image_20250829221547.png](/Imagenes/Pasted_image_20250829221547.png)
y vamos a historico y la intercepcion por post del correo la mandamos al repeater
![Pasted_image_20250829222000.png](/Imagenes/Pasted_image_20250829222000.png)
tal que si le damos send se mandara una nueva contraseña pero vamos a darle a raw wiev
![Pasted_image_20250829222100.png](/Imagenes/Pasted_image_20250829222100.png)
vemos que en el formato se tramita una etica href
![Pasted_image_20250829222137.png](/Imagenes/Pasted_image_20250829222137.png)
que podemos hacer en este punto pues en el repeater ademas de añadir cabeceras nosotro podemos señalar puertos esto se hace en el host
![Pasted_image_20250829222446.png](/Imagenes/Pasted_image_20250829222446.png)
y lo vemos reflejado aqui
![Pasted_image_20250829222526.png](/Imagenes/Pasted_image_20250829222526.png)
pero que pasa si nosotros ponemos unas etiquetas que vallan dirigidas al exploit server y tratamos de obtener la contraseña de carlos
![Pasted_image_20250829223019.png](/Imagenes/Pasted_image_20250829223019.png)
y esto lo podemos ver en los acces logs
![Pasted_image_20250829223147.png](/Imagenes/Pasted_image_20250829223147.png)
probamos la contraseña
![Pasted_image_20250829223327.png](/Imagenes/Pasted_image_20250829223327.png)
y hemos tenido exito
![Pasted_image_20250829223353.png](/Imagenes/Pasted_image_20250829223353.png)
