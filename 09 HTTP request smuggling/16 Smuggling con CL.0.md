En esta clase realizamos un ataque de request smuggling tipo CL.0, donde el servidor back-end ignora el encabezado Content-Length en ciertas rutas, permitiendo inyectar una segunda petición dentro del cuerpo de una POST aparentemente legítima.

Tras identificar un endpoint vulnerable (por ejemplo, /resources/images/blog.svg), utilizamos esta vía para smugglear una solicitud que accede al panel de administración. Finalmente, aprovechamos este comportamiento para enviar una petición oculta que elimina al usuario carlos, completando así el laboratorio con éxito.

Solucion
primero vamos a interceptar cualquier post
y configuramos el primer payload attack
![Pasted_image_20250809230302.png](Imagenes/Pasted_image_20250809230302.png)
(importante poner en automatico la opcion de conten length)
Lo siguiente seria interceptar el home pero sin modificar nada
![Pasted_image_20250809230421.png](Imagenes/Pasted_image_20250809230421.png)
entonces vamos a ser un grupo con los 2
![Pasted_image_20250809230505.png](Imagenes/Pasted_image_20250809230505.png)
![Pasted_image_20250809230738.png](Imagenes/Pasted_image_20250809230738.png)
y ya que tenemos el grupo pasamos hace un ataque multiple
![Pasted_image_20250809230836.png](Imagenes/Pasted_image_20250809230836.png)
