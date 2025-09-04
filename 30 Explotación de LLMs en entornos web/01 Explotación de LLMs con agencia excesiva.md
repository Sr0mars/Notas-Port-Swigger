En esta clase interactuamos con una API LLM que tiene acceso al sistema de base de datos mediante una función de depuración. A través de la conversación con el modelo, identificamos que podemos ejecutar consultas SQL arbitrarias mediante la Debug SQL API. Primero enumeramos los usuarios con un **SELECT**, confirmamos la existencia del usuario carlos y luego emitimos un **DELETE** desde el propio modelo para eliminarlo.

Esto demuestra cómo una exposición excesiva de capacidades en modelos LLM puede llevar a vulnerabilidades críticas.

Solucion
![Pasted_image_20250902112928.png](Imagenes/Pasted_image_20250902112928.png)
La web:
![Pasted_image_20250902113039.png](Imagenes/Pasted_image_20250902113039.png)
vemos que tenemos un chat live y comenzamos una conversacion
![Pasted_image_20250902113328.png](Imagenes/Pasted_image_20250902113328.png)
podemos ver que nos da info asi que vamos a pedirle que nos de infomacion de una tabla
![Pasted_image_20250902113418.png](Imagenes/Pasted_image_20250902113418.png)
asique me ha dado interpretado la query y la infomacion asi que ahora vamos a eliminar al usuario carlos
![Pasted_image_20250902113616.png](Imagenes/Pasted_image_20250902113616.png)
