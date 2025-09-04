En esta clase trabajamos con una configuración CL.TE (Content-Length y Transfer-Encoding) donde el servidor frontal no acepta codificación chunked, pero el servidor trasero sí lo hace. El objetivo es confirmar si es posible inyectar una petición maliciosa al back-end mediante HTTP request smuggling y observar una diferencia en la respuesta como prueba de éxito.

Para ello, enviamos una primera petición que contiene una carga smuggleada que incluye una petición embebida hacia /404. Si el ataque funciona correctamente, al enviar una segunda petición a la raíz del sitio (/), el servidor responderá con un 404, lo que indica que la petición anterior fue procesada de forma inesperada por el back-end.

Esta técnica se basa en una diferencia en la interpretación de los encabezados ‘**Content-Length**‘ y ‘**Transfer-Encoding**‘ entre ambos servidores, lo que permite desincronizar las sesiones HTTP y comprobar la vulnerabilidad a través del comportamiento diferencial.

Solucion
Que es
![Pasted_image_20250805204357.png](/Imagenes/Pasted_image_20250805204357.png)
![Pasted_image_20250805204445.png](/Imagenes/Pasted_image_20250805204445.png)
![Pasted_image_20250805204616.png](/Imagenes/Pasted_image_20250805204616.png)
