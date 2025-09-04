En esta clase analizamos cómo acceder a información sensible oculta mediante consultas manuales en una API GraphQL. A través del historial de peticiones observamos que los posts se consultan por identificadores secuenciales, y notamos que el ID 3 está ausente, lo que sugiere que hay una entrada oculta.

Usamos Burp Suite para enviar una introspection query y descubrimos que el tipo ‘**BlogPost**‘ incluye un campo ‘postPassword’. Modificando manualmente la consulta GraphQL para apuntar al post con ID 3 y solicitando ese campo, extraemos la contraseña asociada.

Esta clase muestra cómo GraphQL puede filtrar información sensible si no se aplican restricciones adecuadas a los campos expuestos y a las consultas realizadas por el cliente.

Solucion
![Pasted image 20250901013144.png](imagenes/Pasted image 20250901013144.png)
![Pasted image 20250901013301.png](imagenes/Pasted image 20250901013301.png)
La web:
![Pasted image 20250901013504.png](imagenes/Pasted image 20250901013504.png)
si nos vamos al BS vemos una peticion post que se esta haciendo al graphql lo mandamos al repeater
![Pasted image 20250901013707.png](imagenes/Pasted image 20250901013707.png)
vemos que se nos pone una nueva pestaña
![Pasted image 20250901013827.png](imagenes/Pasted image 20250901013827.png)
bueno si nos vamos a cualquier post y lo mandamos al repeater
en la cual ahora con la pestaña podemos ver la estructura de como esta hecha y abajo vemos que esta el id
![Pasted image 20250901014134.png](imagenes/Pasted image 20250901014134.png)
que pasa si ponemos el 3 que faltaba
![Pasted image 20250901014312.png](imagenes/Pasted image 20250901014312.png)
entonces si hacemos una querry especifica que nos de la info a lo mejor podemos encontrar el campo especifico
como lo hacemos
nos vamos a la primera peticion post  que hicimos osea la raiz y le damos click derecho, graphql, y ponemos set introspection query
![Pasted image 20250901014524.png](imagenes/Pasted image 20250901014524.png)me realiza una estructura mas grande
![Pasted image 20250901014642.png](imagenes/Pasted image 20250901014642.png)
y si nosotros en la respuesta filtramos por password
![Pasted image 20250901014849.png](imagenes/Pasted image 20250901014849.png)
vemos que nos contempla el campo asi que el campo completo de postPassword lo vamos a poner en la otra peticion
![Pasted image 20250901015011.png](imagenes/Pasted image 20250901015011.png)
y vemos que nos sale una contraseña y esto lo copiamos y pegamos en la web
![Pasted image 20250901015049.png](imagenes/Pasted image 20250901015049.png)
