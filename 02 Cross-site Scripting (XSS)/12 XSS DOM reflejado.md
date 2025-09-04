En esta clase abordamos un XSS reflejado basado en DOM, donde el servidor refleja datos en una respuesta JSON, y luego una función en el navegador —específicamente una llamada peligrosa— evalúa ese contenido sin validación adecuada.

La funcionalidad vulnerable está en el buscador del sitio. Al realizar una búsqueda, el término ingresado se refleja en un archivo JSON de resultados. Este contenido es posteriormente procesado por un script que usa una función que interpreta dinámicamente texto como si fuera código, abriendo la puerta a una inyección si no se escapan correctamente ciertos caracteres.

Aunque el sistema escapa comillas, no hace lo mismo con otros símbolos clave, como la barra invertida. Esto nos permite construir un valor malicioso que rompe la estructura del objeto y añade una instrucción personalizada, haciendo que se ejecute directamente en el navegador.

Este laboratorio muestra cómo una cadena aparentemente segura puede convertirse en un vector de ejecución de código si se mezcla con funciones peligrosas como la evaluación directa de datos, reforzando la importancia de evitar el uso de estas prácticas en el desarrollo web moderno.

Solucion
Aqui no vemos nada de tecnologias aunque el apartado de search es el vulnerable
![[Pasted image 20250708180016.png]]
asi que pasamos a probar payloads
![[Pasted image 20250708180237.png]]
otro
![[Pasted image 20250708180313.png]]
nada aun probamos con la palabra trsting y verificamos las comillas cerramos la equiqueta pero no encontramos nada
![[Pasted image 20250708180507.png]]
podemos ver que en apartado script esta haciendo llamada a una funcion
curl -s -X GET 'https://0a5400d60363e479817bcf1500e80046.web-security-academy.net/resources/js/searchResults.js'   
y aqui nos podemos fijiar en la estructura path que esta disfrazada que en realidad es search-results y tambien en cuenta eval que es vulnerable
![[Pasted image 20250708181748.png]]
y con la ayuda del BS si nos vamos al reapeter podes utilizar operatorias para mandar un codigo malicioso
![[Pasted image 20250708182617.png]]
en este caso se representaria asi en el search 
probando\"*alert(0)}//
![[Pasted image 20250708182834.png]]

