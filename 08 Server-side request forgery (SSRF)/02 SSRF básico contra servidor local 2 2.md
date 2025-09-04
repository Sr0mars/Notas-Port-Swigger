En esta clase continuamos con el mismo laboratorio anterior, donde explotamos una vulnerabilidad SSRF en la funcionalidad de stock. Ya demostramos que era posible acceder al panel de administración interno, y ahora profundizamos en cómo automatizar la interacción con rutas internas específicas.

El objetivo en esta parte es enviar una solicitud manipulada desde el parámetro vulnerable para ejecutar una acción concreta: eliminar al usuario carlos desde el panel de administración. Esto demuestra cómo un SSRF básico puede escalar rápidamente en impacto si se accede a funciones internas críticas del servidor.

Solucion
La web
![Pasted image 20250804185224.png](imagenes/Pasted image 20250804185224.png)
vamis a interceptar check stock con BS y lo mandamos al repeater
![Pasted image 20250804185301.png](imagenes/Pasted image 20250804185301.png)
bueno en el BS vemos que tenemos un stock api qur significa esto que podemos modificar la url para hacer algun tipo de enumeracion
![Pasted image 20250804185551.png](imagenes/Pasted image 20250804185551.png)
de esta menera podemos tener un pequeño acceso
![Pasted image 20250804185955.png](imagenes/Pasted image 20250804185955.png)
y en esta ocacion nos piden que borremos a carlos y bueno lo logramos diriginedo la url donde se encuentra la opcion en el pretty
![Pasted image 20250804190146.png](imagenes/Pasted image 20250804190146.png)
y que hacemos modificamos la url le de damos send por que por afuera nostros no podemos
![Pasted image 20250804190347.png](imagenes/Pasted image 20250804190347.png)
