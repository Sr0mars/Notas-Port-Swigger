En esta clase aplicamos la técnica de HTTP request smuggling con una combinación CL.TE para evadir controles de acceso impuestos por el front-end. El objetivo es acceder al panel de administración, normalmente restringido, y eliminar al usuario carlos desde el back-end.

Para ello, construimos una petición maliciosa que el front-end interpreta como finalizada tras leer los bytes indicados por Content-Length, pero que en realidad contiene una segunda petición HTTP embebida. Esta segunda petición es procesada por el back-end de forma independiente y sin las restricciones del front-end, lo que nos permite interactuar con rutas protegidas como /admin o /admin/delete.

La clase muestra cómo ajustar los encabezados y las longitudes para lograr que la cabecera ‘**Host: localhost**‘ se procese correctamente dentro del cuerpo smuggled, permitiendo así la ejecución de acciones administrativas que normalmente estarían bloqueadas.

Solucion
solamente eliminamos el usuario por get siguiendo los pasos de las otras clases recordar darle a send 2 veces
![Pasted image 20250806215344.png](imagenes/Pasted image 20250806215344.png)
payload (POST / HTTP/1.1

Host: 0abf002c03807acc80c00892005900ab.web-security-academy.net

Content-Length: 90

Transfer-Encoding: chunked



0



GET /admin/delete?username=carlos HTTP/1.1

Host: localhost

Content-Length: 10



x=)
