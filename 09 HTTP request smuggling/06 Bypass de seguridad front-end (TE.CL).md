En esta clase explotamos una vulnerabilidad TE.CL (Transfer-Encoding + Content-Length) para realizar HTTP request smuggling y evadir las restricciones de acceso impuestas por el front-end. El objetivo es acceder a rutas protegidas como /admin o /admin/delete que no están disponibles directamente desde el navegador.

Utilizamos una petición malformada con codificación chunked para engañar al front-end y que interprete una longitud de contenido más corta de lo que realmente se está enviando. Esto permite que el back-end procese una segunda petición embebida que el front-end nunca llega a validar.

Durante la clase, mostramos cómo construir y ajustar la petición smuggled para que incluya la cabecera ‘**Host: localhost**‘, necesaria para que el back-end acepte la acción administrativa. Finalmente, modificamos la ruta de la petición interna para ejecutar la eliminación del usuario carlos y resolver el laboratorio con éxito.

Solucion
hay que quitar algo del BS para que no lo sobreescriba
![[Pasted image 20250806222912.png]]
payload
![[Pasted image 20250806223045.png]]
