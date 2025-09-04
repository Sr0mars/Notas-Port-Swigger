El sistema bloquea el acceso directo a /admin, pero al modificar la cabecera ‘**X-Original-URL**‘ desde Burp, el backend interpreta esta ruta ignorando el filtrado del frontend. Aprovechamos esta característica para acceder primero al panel y luego invocamos ‘**/admin/delete?username=carlos**‘ usando la misma técnica para eliminar al usuario.

Esta clase muestra cómo una mala configuración de cabeceras puede comprometer totalmente la seguridad de la aplicación.

Solucion
entonces lo primero que debemos hacer es tratar de ver si nos podemos ir al la seccion de admin
![Pasted_image_20250815185957.png](Imagenes/Pasted_image_20250815185957.png)
obiamente nos va salir que acceso denegado
![Pasted_image_20250815190038.png](Imagenes/Pasted_image_20250815190038.png)
por lo cual vamos a interceptarlo
![Pasted_image_20250815190151.png](Imagenes/Pasted_image_20250815190151.png)
lo que podemos hacer es irnos a la raiz y jugar con la cabecera X-Original-URL
![Pasted_image_20250815190613.png](Imagenes/Pasted_image_20250815190613.png)
entonces ya solo seria copiar la url pero antes tenemos que partir eso
![Pasted_image_20250815190809.png](Imagenes/Pasted_image_20250815190809.png)
por que si no da problema

