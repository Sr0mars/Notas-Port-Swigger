Este laboratorio presenta un fallo en la validación del encabezado Referer que permite llevar a cabo un ataque CSRF. Aunque el servidor intenta bloquear peticiones que provienen de dominios cruzados, su validación es deficiente y permite cualquier valor de Referer que contenga el dominio legítimo en cualquier parte de la cadena.

Para explotarlo, se fuerza al navegador de la víctima a generar una petición con un Referer modificado, incluyendo el dominio legítimo como parte de una query string. Esto se logra manipulando la URL del historial con history.pushState para incorporar el dominio objetivo en la cadena.

Dado que los navegadores modernos suelen eliminar la query string del encabezado Referer por defecto, es necesario forzar su inclusión estableciendo la política de referrer como unsafe-url mediante el encabezado Referrer-Policy en el exploit. De esta forma, se consigue que el servidor acepte la petición y se complete el cambio de correo.

Este escenario demuestra cómo una validación parcial y mal implementada del encabezado Referer puede dejar la aplicación vulnerable a ataques CSRF.

Solucion
Al igual que en los otros laboratorios lo que realizamos es lo mismo cambiamos el correo lo interceptamos
y pues vemos que no obtenemos ninguna restriccion al csrf
![Pasted image 20250723232459.png](imagenes/Pasted image 20250723232459.png)
de principio si enviamos un payload sencillo no nos dejara por la restriccion de referer uqe no esta proviniendo de la misma url
![Pasted image 20250723232745.png](imagenes/Pasted image 20250723232745.png)
en este punto lo que podemos hacer es buscar como engañar al propio referer ya que esta es una politica que tiene los navegadores como mecanismo de seguridad asi que lo que podemos hacer es buscar otro ripo de sintaxis
![Pasted image 20250723233239.png](imagenes/Pasted image 20250723233239.png)

Referrer-Policy: unsafe-url
con esa politica burlamos ese proceso
![Pasted image 20250723235941.png](imagenes/Pasted image 20250723235941.png)

por lo cual podemos cambiarle el correo
