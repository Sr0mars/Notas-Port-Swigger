Esta clase continúa el laboratorio anterior y se centra en repetir el envenenamiento de la cola de respuestas (response queue poisoning) para capturar la cookie de sesión del administrador en el momento exacto en el que inicia sesión.

Aprovechando que el servidor backend sigue procesando peticiones HTTP/1.1 embebidas dentro de solicitudes HTTP/2, enviamos varias peticiones preparadas con un GET /x camuflado. Gracias a este desfase, logramos obtener la respuesta de otra sesión, la del administrador. Si conseguimos capturar una respuesta con código 302 y una cookie válida, podemos usarla para acceder a /admin.

Una vez en el panel de administración, podremos identificar la URL para borrar a carlos y así completar el laboratorio.

Esta fase requiere paciencia y precisión, ya que dependemos del momento en que el administrador realice su acción.

Solucion
Entonces aqui lo que queremos es forzar un estado de error 302 (se necesita poner varios sends)
![Pasted_image_20250809210616.png](Imagenes/Pasted_image_20250809210616.png)oQWrcEUugh4yROOhI52xKkdpQukn3SCJ
y nos copiamos la coockie del admin
![Pasted_image_20250809211248.png](Imagenes/Pasted_image_20250809211248.png)
la pegamos y eliminamos el usuario carlos en el admin panel
