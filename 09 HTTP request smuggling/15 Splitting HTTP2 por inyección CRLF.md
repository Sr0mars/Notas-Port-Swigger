En esta clase explotamos una vulnerabilidad de request splitting específica de HTTP/2, en la que el servidor no limpia correctamente los caracteres de control inyectados en las cabeceras. Inyectamos una secuencia CRLF en el valor de una cabecera para fragmentar la petición HTTP, smugglear una nueva solicitud y envenenar la cola de respuestas.

Con este ataque, esperamos a que el usuario administrador inicie sesión. Capturamos su sesión mediante un código 302 redirigiéndolo a su panel, reutilizamos su cookie y finalmente eliminamos al usuario carlos para completar el laboratorio.

Solucion
vamos a interceptar la pagina principal e interpetamos hacemos solamente el change method y lo siguien es hacer pruebas pero vamos que no funcionan asi que vamos a probar lo mismo del laboratorio anterior con el tranfer
![[Pasted image 20250809222828.png]]
hacemos el mismo proceso y le damos add
![[Pasted image 20250809223011.png]]
y le damos send
![[Pasted image 20250809223049.png]]
pero vemos que no nos da ningun error asi que lo siguiente es borrar de nueva esa cabecera que metimos
entonces lo hacemos por GET pero por GET nos sale otro error
(value



GET /error HTTP/1.1

Host: 0a6500b5035e9422806d26a800790066.web-security-academy.net)
![[Pasted image 20250809223350.png]]
asi que vamos a meter otra cabecera y vamos a modificar el raw
asi quedaria el Raw
![[Pasted image 20250809223952.png]]
y asi quedaria el la cebezera que vamos a meter
![[Pasted image 20250809224058.png]]
entonces le damos a send unas 3 o 2 veces hasta que veamos el error
![[Pasted image 20250809224212.png]]
entonces nosotros necesitamos darle de nuevo a send hasta que nos salga el  error 302 y ahi obtenemos la cookie
![[Pasted image 20250809224928.png]]
nos copiamos la cookie y la pegamos  y eliminamos al usuario carlos
![[Pasted image 20250809225002.png]]

