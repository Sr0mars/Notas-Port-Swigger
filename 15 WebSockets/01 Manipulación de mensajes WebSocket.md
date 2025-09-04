Este laboratorio demuestra cómo se puede abusar del canal de comunicación WebSocket para introducir cargas maliciosas que no pasan por los filtros del navegador.

La aplicación cuenta con un chat en tiempo real gestionado por WebSockets. Al enviar un mensaje desde el navegador, observamos que el cliente aplica una codificación automática para evitar ataques. Sin embargo, al interceptar el mensaje desde una herramienta como Burp y modificarlo manualmente antes de que llegue al servidor, conseguimos insertar una carga que, al ser procesada por el navegador del agente de soporte, genera una ejecución no deseada.

Esta técnica pone de manifiesto la importancia de validar los mensajes en el servidor, ya que las protecciones del cliente pueden ser fácilmente eludidas. El laboratorio se completa cuando logramos que la carga manipulada sea procesada por el navegador del agente, confirmando la existencia de la vulnerabilidad.

Solucion
![[Pasted image 20250820234433.png]]
La web:
![[Pasted image 20250820234527.png]]
y tenemos un chat en linea
![[Pasted image 20250820234631.png]]
esto es lo que vemos en el http history 
![[Pasted image 20250820234736.png]]
pero no es lo mismo si nos vamos en el websocket del propio BS podemos ver esto
![[Pasted image 20250820234936.png]]
si nosotros interceptmaos un hola en el live chat
![[Pasted image 20250820235033.png]]
y lo mandamos al repeter
y lo modificamos por una alerta
![[Pasted image 20250821000427.png]]