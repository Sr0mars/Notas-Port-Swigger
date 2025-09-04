En esta clase llevamos a cabo un ataque de Cross-Site WebSocket Hijacking (CSWSH) para obtener el historial de chat de una víctima, el cual incluye su usuario y contraseña en texto claro.

La clave está en que la cookie de sesión del sitio tiene la directiva SameSite=Strict, lo que bloquea el uso de cookies en peticiones entre sitios distintos. Sin embargo, el mismo dominio tiene una versión hermana (cms…) vulnerable a XSS, y ambos comparten el mismo site (por definición de navegador).

Esto nos permite lanzar el ataque desde el dominio hermano sin que SameSite lo bloquee. Aprovechamos la XSS reflejada en el login del dominio cms para inyectar un payload JavaScript que establece una conexión WebSocket legítima con el dominio original, simulando el mensaje READY, y exfiltrando la respuesta a un servidor externo (Burp Collaborator).

Esta lección muestra una técnica muy poderosa para eludir restricciones de SameSite y exfiltrar información sensible usando WebSockets en aplicaciones que no implementan protecciones adecuadas.

Solucion
