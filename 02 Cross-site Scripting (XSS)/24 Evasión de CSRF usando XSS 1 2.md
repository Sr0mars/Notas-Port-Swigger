En esta clase explotamos un XSS almacenado para ejecutar una acción que normalmente estaría protegida por medidas anti-CSRF. La aplicación permite insertar comentarios maliciosos que se ejecutan cuando otro usuario visita el blog, lo que nos permite acceder a sus sesiones activas y realizar acciones en su nombre.

Nuestro objetivo es cambiar la dirección de correo electrónico del usuario afectado. Para ello, necesitamos primero obtener el token CSRF válido que protege dicha operación. Aprovechamos el XSS para hacer una petición al área de configuración de cuenta, capturar el contenido de la respuesta y extraer el token desde el HTML.

Una vez que tenemos el token, generamos una segunda petición desde el navegador de la víctima, enviando el token y la nueva dirección de correo. Como todo ocurre dentro de su propia sesión, la operación se realiza con éxito.

Este laboratorio demuestra cómo un XSS puede romper las defensas de tipo CSRF y subraya la importancia de que los tokens no solo estén presentes, sino que también estén correctamente aislados del acceso por parte de scripts inyectados.

Solucion
Lo primero seria interceptar el cambio de correr por medio de BS esto cosiderando que tenemos un correo y queremos cambiarlo
![Pasted_image_20250717173453.png](/Imagenes/Pasted_image_20250717173453.png)
dentro del BS lo mandamos al repeater y es una peticion post por lo cual vamos a URLuncodear y en la peticcion podemos ver el csrf que unico para cada cuenta
![Pasted_image_20250717173807.png](/Imagenes/Pasted_image_20250717173807.png)

esto es algo que podemos ver en el codigo fuente
![Pasted_image_20250717174233.png](/Imagenes/Pasted_image_20250717174233.png)
ahora lo que podemos hacer es un script el cual me retorne esta csrf con la ayuda de BS collaborator

