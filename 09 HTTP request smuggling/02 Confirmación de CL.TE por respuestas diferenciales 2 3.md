En esta clase continuamos con el mismo laboratorio anterior, en el que identificamos una vulnerabilidad de HTTP request smuggling basada en CL.TE (Content-Length + Transfer-Encoding). Mantenemos el mismo enfoque, pero seguimos profundizando en cómo se comporta el servidor al recibir múltiples peticiones dentro del mismo cuerpo HTTP.

El objetivo sigue siendo verificar que el ataque permite alterar la interpretación del contenido por parte del servidor de backend, forzando un error o manipulando las respuestas. Esta parte sirve como puente hacia la tercera y última sección del laboratorio, donde finalmente aprovecharemos este comportamiento para lograr el impacto deseado.

Solucion
![Pasted_image_20250805205008.png](/Imagenes/Pasted_image_20250805205008.png)
![Pasted_image_20250806191531.png](/Imagenes/Pasted_image_20250806191531.png)
La web:
![Pasted_image_20250806191934.png](/Imagenes/Pasted_image_20250806191934.png)
Vamos a interceptarla con BS una ves dentro vmaos a cambiar el request atribut en la parte derecha a http 1 y cambiamos el metodo de GET a POST
![Pasted_image_20250806192132.png](/Imagenes/Pasted_image_20250806192132.png)
una vez realizado esto vamos a limpiar y quedarnos solo lo que necesitamos
![Pasted_image_20250806192331.png](/Imagenes/Pasted_image_20250806192331.png)
una breve explicacion del payload
POST / HTTP/1.1
Host: YOUR-LAB-ID.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
Content-Length: 35
Transfer-Encoding: chunked

0

GET /404 HTTP/1.1
X-Ignore: X)

💥 ¿Qué está intentando hacer este payload?
Este es un ataque de desincronización de petición-respuesta HTTP o HTTP Request Smuggling, también conocido como "smuggling attack". El atacante intenta inyectar una petición HTTP adicional dentro de la primera, rompiendo la manera en que los servidores intermedios (como proxies, balanceadores de carga o firewalls) interpretan las peticiones.

🧠 ¿Cómo funciona?
1. Encabezados clave en la petición:
Transfer-Encoding: chunked
Se usa para indicar que el cuerpo del mensaje será enviado en fragmentos (chunks), y anula el Content-Length en muchos servidores.

Content-Length: 35
Normalmente indica el tamaño del cuerpo, pero al incluir también Transfer-Encoding, se genera un conflicto. Algunos servidores priorizan Content-Length, otros Transfer-Encoding.

Este conflicto es la base del ataque.

2. El cuerpo del mensaje empieza así:

0
Esto indica que el cuerpo en formato chunked ha terminado inmediatamente (el 0 significa "no hay más chunks").

3. Y luego, dentro del cuerpo, se añade otra petición HTTP:
makefile

GET /404 HTTP/1.1
X-Ignore: X)
Esto es una petición GET "oculta", inyectada en el cuerpo del mensaje POST. Lo que se busca es que:

El proxy (o balanceador) vea solo el primer POST y lo procese correctamente.

Pero el servidor de back-end vea también la segunda petición GET /404 como una petición nueva.

Esto puede causar que:

El back-end ejecute el GET /404 como si fuera una nueva solicitud.

La siguiente petición legítima que haga un usuario reciba la respuesta de esa petición maliciosa (es decir, desincronización).

Se logre inyectar tráfico malicioso o robar datos de otros usuarios.

🧪 ¿Qué busca el atacante?
El objetivo no es hacer una petición 404, sino ver si el sistema es vulnerable a HTTP Request Smuggling. Usan /404 porque es una ruta que siempre devuelve algo, y permite saber si la petición fue procesada.

Si el atacante ve que su GET /404 aparece ejecutado sin que él lo haya solicitado directamente, entonces el sistema está interpretando mal las peticiones y es vulnerable a desincronización.

🧨 ¿Por qué es peligroso?
Un atacante puede usar esto para:

Bypassear firewalls.

Interceptar respuestas de otros usuarios.

Ejecutar comandos maliciosos en el servidor back-end.

Realizar cache poisoning, XSS, etc.


🧱 Resumen
Parte	Descripción
Transfer-Encoding: chunked	Se usa para enviar el cuerpo en fragmentos. Confunde a algunos servidores.
0	Indica que no hay más fragmentos (termina el cuerpo chunked).
GET /404 HTTP/1.1	Se inyecta como si fuera una nueva petición HTTP.
Resultado	Puede causar que el backend lo interprete como una nueva solicitud.
