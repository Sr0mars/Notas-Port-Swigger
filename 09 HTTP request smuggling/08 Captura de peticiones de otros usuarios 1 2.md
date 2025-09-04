En esta clase realizamos un ataque de tipo HTTP request smuggling con el objetivo de interceptar las peticiones de otros usuarios que interactúan con la aplicación. Aprovechamos la desincronización entre el front-end y el back-end para almacenar la petición del siguiente usuario como parte de nuestra propia publicación de comentario.

Modificamos la petición original de publicación de comentario para incluir una petición smuggled hacia el mismo endpoint. Aumentamos manualmente el valor de ‘**Content-Length**‘ para que el servidor backend interprete parte de la siguiente petición del usuario como si fuera nuestra, y la almacene junto a nuestro comentario.

Cuando el siguiente usuario interactúe con la aplicación, su petición será interceptada y guardada en nuestro comentario. Visualizando dicho comentario, podremos obtener su cookie de sesión, la cual nos permitirá acceder directamente a su cuenta.

Este tipo de ataque simula situaciones reales donde un atacante podría capturar credenciales o tokens de otros usuarios, y destaca la peligrosidad de las desincronizaciones entre capas de infraestructura HTTP.

Solucion
esta vulnerabilidad se encuentra en la parte de la seccion de comentarios por lo cual pasamos a interceptar y hacemos la configuracion de http 1.1 y la de cambiar el metodo de get a post y cambiar a la cabecera a la raiz
![Pasted_image_20250807215013.png](Imagenes/Pasted_image_20250807215013.png)
asi que para poder empezar a acomadar nuestro payload primero vamos a interceptar una solicitud de la seccion de comentarios nos quedmaos con el content-length , content-type y el csrf de la victima
![Pasted_image_20250807215900.png](Imagenes/Pasted_image_20250807215900.png)
ahora lo que necesitamos es la cookie de session asi que vmaos a interceptar la pagina princiapal pensando que nosotros estamos logeados para obtener la cookie