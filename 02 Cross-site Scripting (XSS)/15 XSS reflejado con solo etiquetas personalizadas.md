En esta clase enfrentamos un entorno con XSS reflejado donde la aplicación ha bloqueado por completo todas las etiquetas HTML estándar, permitiendo únicamente etiquetas personalizadas. Este tipo de configuración busca prevenir inyecciones, pero aún puede ser burlada si no se filtran los atributos o eventos correctamente.

Utilizamos un servidor de explotación para construir un vector que incluye una etiqueta inventada, con un identificador específico y un evento que se activa al enfocar ese elemento. Al añadir un fragmento al final de la URL que apunta a esa etiqueta personalizada, el navegador intenta enfocarla automáticamente al cargar la página, lo que desencadena la ejecución del código malicioso sin necesidad de interacción del usuario.

Este laboratorio demuestra cómo incluso etiquetas no estándar pueden ser vehículos válidos para ataques XSS si los atributos y eventos no son controlados adecuadamente, reforzando la importancia de validar todo el contenido, no solo el nombre de la etiqueta.

URL

Solucion

Aqui nosotros haremos nuestro propia tag
En este caso no servira lo anterior que hicimos pero podemos utilizar una etiqueta la cual se llama onfocus

<script>
location = 'https://0a0200b404e409a680c5f3cb006400c0.web-security-academy.net/?search=<etiqueta id=x onfocus=alert(document.cookie) tabindex=1>#x';
</script>