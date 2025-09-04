Con la base sentada en la clase anterior, en esta parte se lleva a cabo la explotación directa del fallo. El atacante almacena en el exploit server un archivo JavaScript con una carga maliciosa (como una alerta con las cookies del usuario).

Luego, vuelve a realizar una petición manipulada a la home del sitio, esta vez sin parámetro de cache-busting, y utilizando de nuevo la cabecera ‘**X-Forwarded-Host**‘, esta vez apuntando al exploit server. Una vez confirmada la cacheabilidad de la respuesta, se espera que el próximo visitante habitual de la página reciba la versión envenenada y ejecute el código malicioso en su navegador.

Esta clase culmina demostrando cómo una cabecera mal gestionada puede ser la puerta de entrada a ataques persistentes del lado del cliente a través de la infraestructura de caché del propio sitio.

Solucion

La web:
![[Pasted image 20250821201044.png]]
Vamos a interceptar y para envenenar el cache se puede hacer una cabecera previo a eso podemos instalar una extencion la cual nos ayudara a poder adivinar la cabecera la cual se llama (Param miner)
![[Pasted image 20250821201615.png]]
el cual se va emplear la cabecera X-Forwarded-Host: en este caso
![[Pasted image 20250821202035.png]]
el cual se va emplear en la espuesta una ves le demos a send
asi que como tenemos un exploit server podemos utilizarlo
![[Pasted image 20250821202314.png]]
ahora solo configuramos la cabecera con la url de nuestro exploit server
![[Pasted image 20250821202458.png]]
y ya solo recargamos la pagina
![[Pasted image 20250821202529.png]]
