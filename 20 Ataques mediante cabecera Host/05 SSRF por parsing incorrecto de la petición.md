Esta clase explora un caso de Server-Side Request Forgery (SSRF) basado en un fallo de parsing que ocurre cuando la aplicación analiza mal el destino real de la petición al recibir una URL absoluta en lugar de usar solo el valor de la cabecera Host.

El laboratorio permite el acceso al panel interno de administración ubicado en una IP del rango 192.168.0.0/24. Aunque el servidor bloquea los intentos de modificar directamente la cabecera Host, se descubre que al emplear una URL absoluta en la línea de la petición (por ejemplo, GET https://host/), se puede forzar al middleware a redirigir la petición basándose en esa URL, ignorando el valor de la cabecera Host.

Se utiliza Burp Collaborator para verificar que efectivamente el backend realiza peticiones hacia dominios arbitrarios incluidos en esa línea. Luego, mediante Burp Intruder, se fuerza una enumeración de direcciones IP internas hasta encontrar la del panel /admin.

Una vez encontrado, se obtiene el token CSRF y la cookie de sesión del panel, y se construye una petición manual POST apuntando a /admin/delete con los parámetros correctos para eliminar al usuario carlos.

Esta clase enseña cómo los errores en la validación del destino de la petición —en concreto, aceptar URLs absolutas sin una validación estricta del destino— pueden provocar exposiciones críticas mediante SSRF, incluso en entornos teóricamente aislados.

Solucion
