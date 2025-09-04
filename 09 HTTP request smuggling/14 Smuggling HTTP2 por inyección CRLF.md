En esta clase llevamos a cabo un ataque de HTTP/2 request smuggling aprovechando una mala sanitización de cabeceras por parte del front-end. Usamos un vector exclusivo de HTTP/2 basado en inyección CRLF dentro del valor de una cabecera, lo que nos permite introducir una cabecera ‘**Transfer-Encoding: chunked**‘ maliciosa y un cuerpo que termina en 0.

Este smuggling provoca que el backend procese parcialmente nuestra petición y mezcle el siguiente request del usuario víctima con la cola de respuestas, exponiendo su sesión en nuestro historial de búsquedas. Capturamos su token de sesión, lo reutilizamos, y accedemos a su cuenta para completar el laboratorio.

Solucion
vemos que en la pagina principal en la parte de busquedad se queda alamacena nuestra consultas y vemos que tambien se quedan las coockies
![Pasted image 20250809214953.png](imagenes/Pasted image 20250809214953.png)
![Pasted image 20250809215022.png](imagenes/Pasted image 20250809215022.png)
por lo cual nos podemos aprovechamos de esto asi que vmaos a interceptar por lo cual significa que la busquedad esta vinculada con la cookie de session
por lo cual hay que recargar la pagina hasta que nos salga get y ese lo mandamos al repeater (ya estando en el repeater hacemos la configuracion de change method)
![Pasted image 20250809220229.png](imagenes/Pasted image 20250809220229.png)
Bueno aqui probamos de todo pero nada funciono asi que lo que podemos hacer es aprovecharnos de las cabezeras si no estan bien sanitizadas
![Pasted image 20250809220520.png](imagenes/Pasted image 20250809220520.png)
que pasa aqui bueno aqui lo que hacemos es agregar una cabezera nuesta en el apartado de request headers le damos al + bueno ponemos en la parte de value test(shift+enter) y copiamos la cabecera que quitamos en el Raw que en este caso fue el trasnfer encoding
asi que le damos add y mandmaos 2 veces el send y nos manda el error 404
![Pasted image 20250809221105.png](imagenes/Pasted image 20250809221105.png)

esto significa que ya ah funcionado por lo cual ahora podemos hacer nuestro payload para ello vamos a interceptar nuevamente la pagina pero unicamente para obtener la cookie de session
![Pasted image 20250809221353.png](imagenes/Pasted image 20250809221353.png)
SyfzoXSoekovnGWMKNTVe6gntP5D2d7X
y ahora esta cookie de session la contemplamos en nuestro payload
entonces vamos a modificar el payload
(0



POST / HTTP/1.1

Host: 0a5200520381201482d09c40006d000b.web-security-academy.net

Cookie: session=SyfzoXSoekovnGWMKNTVe6gntP5D2d7X

Content-Length: 850



search=x)
![Pasted image 20250809221949.png](imagenes/Pasted image 20250809221949.png)
y vamos a esperar un poco y nos vamos a la pagina principal y nos aparecera la cookie de session
![Pasted image 20250809221817.png](imagenes/Pasted image 20250809221817.png)
De esta manera solamente modificamos la cookie en la interfaz y ya nos hemos conectado
