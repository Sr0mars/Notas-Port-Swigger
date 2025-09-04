En esta clase aprovechamos una vulnerabilidad de Server-Side Template Injection (SSTI) en Ruby (ERB), donde la aplicación evalúa contenido enviado por el usuario sin validación. Mediante la sintaxis de plantillas de ERB, demostramos la ejecución de código del lado servidor, logrando eliminar un archivo del sistema con un simple payload.

Un ejemplo claro de cómo una mala interpolación de plantillas puede poner en peligro la integridad del servidor.

Solucion
La web:
![Pasted_image_20250814184937.png](Imagenes/Pasted_image_20250814184937.png)
ejemplos
![Pasted_image_20250814185519.png](Imagenes/Pasted_image_20250814185519.png)
si nosotros picamos en cualquier producto podemos notar que en la url se aplica la plantilla en este caso del producto
![Pasted_image_20250814185809.png](Imagenes/Pasted_image_20250814185809.png)
entonces en base a que plantilla este programada en la pagina podemos ir probando payloads
para ello podemos utilizar este recurso
https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Template%20Injection
en este caso se emplea ruby asi que podemos aplicar algunas consultas
![Pasted_image_20250814190246.png](Imagenes/Pasted_image_20250814190246.png)
<%= system("rm /home/carlos/morale.txt") %>
