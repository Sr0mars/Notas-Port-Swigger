El laboratorio presenta una configuración errónea en la que el parámetro ‘**utm_content**‘ no se incluye en la clave de caché debido a una expresión regular mal diseñada. Esto permite modificar valores clave, como el idioma (**lang**), sin invalidar la caché.

Por ejemplo, se puede construir una URL como ‘**/login?lang=en?utm_content=xyz**‘, en la que todo lo posterior a ‘**lang=**‘ no es considerado por la caché pero sí interpretado por el backend. Este comportamiento es el primer paso para una cadena de ataque más compleja.

Solucion
entonces al abrir el laboratorio nos dirige al login
![Pasted image 20250822192752.png](imagenes/Pasted image 20250822192752.png)
en el BS vemos esto
primero la peticion de la raiz
![Pasted image 20250822192924.png](imagenes/Pasted image 20250822192924.png)
podemos ver que es una solicitud simple y se emplea la cache
la segunda los mismo se emplea la solicitud y la cache el cual es un redirect de la propia raiz
![Pasted image 20250822193029.png](imagenes/Pasted image 20250822193029.png)
en la siguiente solicitud curiosamente vemos que no se emplea la cache
![Pasted image 20250822193109.png](imagenes/Pasted image 20250822193109.png)
entonces podemos enviar de primera al repeater el login redirect que seria la segunda captura
bueno investigando un poco si nosotro miramos la tercera captura y checamos el codigo podemos ver que se hace una peticion al de parte del script src
![Pasted image 20250822193751.png](imagenes/Pasted image 20250822193751.png)
lo miramos
y podemos ver que este si se cachea por lo cual lo mandamos la repeater
![Pasted image 20250822193846.png](imagenes/Pasted image 20250822193846.png)
como sabesmos si se cachea?
bueno si miramos el codigo y modificamos el en al hola podemos ver que en la respuesta tenemos un hola por lo cual nos sirve
![Pasted image 20250822194037.png](imagenes/Pasted image 20250822194037.png)
ahora si en loginredirect le damos follow  nos vamos al codigo fuente
![Pasted image 20250822194259.png](imagenes/Pasted image 20250822194259.png)
