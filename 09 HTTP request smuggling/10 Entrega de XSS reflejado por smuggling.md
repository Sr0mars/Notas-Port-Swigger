En este laboratorio, combinamos un ataque de HTTP request smuggling con una vulnerabilidad de XSS reflejado que afecta a la cabecera User-Agent. El objetivo es hacer que la siguiente petición de un usuario legítimo reciba una respuesta que incluya nuestra carga maliciosa.

Para lograrlo, manipulamos la longitud de la petición y ocultamos una petición HTTP secundaria con el ‘**User-Agent**‘ alterado. La víctima, al visitar la aplicación, carga sin saberlo una página que ejecuta JavaScript, concretamente ‘**alert(1)**‘, validando la explotación.

Este escenario pone en evidencia cómo la concatenación de vulnerabilidades aparentemente menores puede tener un impacto crítico cuando son encadenadas correctamente.

Solucion
antes de interceptar necesitamos obtener el user agent para ello nos vamos  a la pagina princial Ctrl+Shift+C y nos vamos al apartado de red o network y en la primera y hasta abajo copiamos y bajamos (https://0a5f004004d306dc80b60dd600330012.web-security-academy.net/)
![Pasted_image_20250809203435.png](Imagenes/Pasted_image_20250809203435.png)
entonces este campo vamos a buscar y bueno lo encontramos en un post 
![Pasted_image_20250809203602.png](Imagenes/Pasted_image_20250809203602.png)
entonces aqui podemos ver un tipo de vulnerabilidad que si escapamos las comillas podemos obtener informacion para ello vamos a interceptar la pagina para ver si es vulnerable con este pequeñp script "><script>alert(1)</script>
![Pasted_image_20250809204328.png](Imagenes/Pasted_image_20250809204328.png)
Entonces es vulnerable a xxs reflejado
![Pasted_image_20250809204355.png](Imagenes/Pasted_image_20250809204355.png)

entonces pasamos hacer el payload
 (Content-Type: application/x-www-form-urlencoded
Content-Length: 150
Transfer-Encoding: chunked

0

GET /post?postId=5 HTTP/1.1
User-Agent: a"/><script>alert(1)</script>
Content-Type: application/x-www-form-urlencoded
Content-Length: 5

x=1)
![Pasted_image_20250809204727.png](Imagenes/Pasted_image_20250809204727.png)
le damos a send y recargamos la pagina
![Pasted_image_20250809204808.png](Imagenes/Pasted_image_20250809204808.png)
