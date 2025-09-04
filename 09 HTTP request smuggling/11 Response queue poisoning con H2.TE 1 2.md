Este laboratorio demuestra cómo un ataque de HTTP request smuggling mediante H2.TE (HTTP/2 → Transfer-Encoding) puede usarse para explotar un desfase en la cola de respuestas entre servidores.

La técnica se basa en inyectar una petición HTTP/1.1 completa dentro del cuerpo de una petición HTTP/2 utilizando ‘**Transfer-Encoding: chunked**‘, lo que provoca que la respuesta a esa petición se “adelante” en la cola. De este modo, cuando un administrador inicia sesión, podemos capturar su respuesta, obtener su cookie de sesión y reutilizarla para acceder al panel de administración.

Una vez dentro, aprovechamos ese acceso para ejecutar la acción que resuelve el laboratorio: eliminar al usuario carlos.

Este escenario combina el downgrade de HTTP/2, el envenenamiento de la cola de respuestas y la captura de sesiones en un entorno realista de request smuggling.

Solucion
entonces para empezar vmaos a interceptar la pagina principal y vamos hacer los cambios pero en este caso no es necesario el http 1.1 por que ya conoce las proporciones del size por lo cual solo ponemos el method
![Pasted_image_20250809205856.png](Imagenes/Pasted_image_20250809205856.png)



