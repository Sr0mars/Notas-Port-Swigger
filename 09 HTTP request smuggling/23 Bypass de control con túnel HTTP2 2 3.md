En esta segunda parte, utilizamos la vulnerabilidad descubierta para realizar una inyección de cabeceras internas y leer su contenido.

A través de una búsqueda manipulada y un cuerpo POST con tamaño superior al declarado, conseguimos hacer que el servidor refleje parte del contenido HTTP real enviado por el cliente, incluyendo cabeceras sensibles como ‘**X-SSL-VERIFIED**‘, ‘**X-SSL-CLIENT-CN**‘ y ‘**X-FRONTEND-KEY**‘. Estos encabezados son fundamentales para emular al usuario administrador en la última etapa del ataque.

Solucion
con este curl te reporta el CL de la aplicacion
![Pasted_image_20250811170635.png](/Imagenes/Pasted_image_20250811170635.png)
pero tambien si hacemos un head en vez de get en el BS nos dice los CL esperados
![Pasted_image_20250811170814.png](/Imagenes/Pasted_image_20250811170814.png)
lo ideal en este caso es que nos reporte menos bites de los cuales esta teniendo pero si lo probamos con la cabecera admin obtenemos un 401
![Pasted_image_20250811171114.png](/Imagenes/Pasted_image_20250811171114.png)
esto lo que quiere decir es que queda algo pendiente para poder ver este recurso
entonces para ver este recurso vamos a interceptar otra ventana en el search y esta ves lo vamos a tramitar por post
![Pasted_image_20250811171756.png](/Imagenes/Pasted_image_20250811171756.png)
entonces que vamos hacer ya que este en post vamos a eliminar estas lineas de codigo y las vamos  a hacer cabeceras
![Pasted_image_20250811171930.png](/Imagenes/Pasted_image_20250811171930.png)
asi quedaria en un principio
![Pasted_image_20250811172102.png](/Imagenes/Pasted_image_20250811172102.png)
le damos add seguido de send (el search va asi search=prueba)
![Pasted_image_20250811172442.png](/Imagenes/Pasted_image_20250811172442.png)
lo que passa aqui es que el fronted se confunda