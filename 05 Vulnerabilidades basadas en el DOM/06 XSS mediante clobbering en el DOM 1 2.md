En esta clase se analiza un caso avanzado de XSS basado en DOM Clobbering, donde el sitio intenta construir un objeto con una variable global utilizando un patrón inseguro: si la variable no existe, se asigna un valor por defecto. Este patrón se vuelve vulnerable cuando un atacante puede introducir elementos HTML con IDs y atributos específicos que sobrescriben esa variable global.

Mediante el uso de etiquetas de ancla duplicadas, se fuerza la creación de una colección DOM que clobberiza el objeto esperado. Además, el atributo name se manipula para inyectar un valor malicioso en la propiedad que más adelante será utilizada por la aplicación.

En este escenario, al cargar una página que intenta acceder a esa variable ya clobberizada, el navegador ejecuta el contenido inyectado, lo que demuestra cómo una lógica aparentemente inofensiva puede ser explotada para ejecutar JavaScript arbitrario sin necesidad de insertar directamente un script visible.

Esta técnica destaca cómo incluso con filtros activos como DOMPurify, ciertos protocolos como ‘**cid:**‘ pueden permitir eludir restricciones y ejecutar código malicioso si el resto de la lógica de la aplicación es insegura.

Solucion
en esta ocacion en la seccion de comentarios si nos fijamos en el codigo fuente nos encontramos con 2 scripts
![Pasted image 20250727210540.png](imagenes/Pasted image 20250727210540.png)
![Pasted image 20250727210405.png](imagenes/Pasted image 20250727210405.png)
