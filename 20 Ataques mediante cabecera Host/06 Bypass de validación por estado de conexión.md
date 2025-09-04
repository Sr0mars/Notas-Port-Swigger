En esta clase se aborda una vulnerabilidad de Server-Side Request Forgery (SSRF) avanzada, donde el servidor valida correctamente la cabecera Host en la primera petición, pero omite esa validación en las siguientes peticiones de la misma conexión. Este tipo de fallo se basa en un mal manejo del estado de conexión y está inspirado en ataques reales descubiertos por PortSwigger, como los Browser-Powered Desync Attacks.

El ataque comienza realizando una petición aparentemente legítima con la cabecera Host apuntando al dominio del laboratorio. A continuación, dentro del mismo canal TCP (mediante “Send group in sequence” en Burp Repeater), se encadena una segunda petición apuntando al host interno 192.168.0.1, específicamente al endpoint /admin.

Debido a la conexión persistente y a que el servidor asumió que todas las peticiones de esa conexión eran válidas tras la primera validación, la segunda petición se enruta internamente sin aplicar la misma validación estricta. Esto permite acceder al panel de administración sin autorización.

Una vez dentro del panel, se recuperan los detalles del formulario (token CSRF, nombre del parámetro username y la ruta /admin/delete) y se construye manualmente una petición POST que, al ser enviada en la misma conexión persistente, permite eliminar al usuario carlos.

Esta clase demuestra cómo una configuración aparentemente segura puede ser comprometida aprovechando comportamientos sutiles del protocolo HTTP y la gestión del estado de las conexiones.

Solucion
Interceptamos el home
y en el repeater vamos a crear un grupo
en el cual el primero vamos a tener
![Pasted_image_20250829212229.png](/Imagenes/Pasted_image_20250829212229.png)
y en el segundo vamos atener este 
![Pasted_image_20250829212249.png](/Imagenes/Pasted_image_20250829212249.png)
y va quedar asi
![Pasted_image_20250829212412.png](/Imagenes/Pasted_image_20250829212412.png)
y podemos ver que en la segunda peticion nos manda una ruta admin
![Pasted_image_20250829212622.png](/Imagenes/Pasted_image_20250829212622.png)
entonces le agregamos el admin en el get nos regresamos a la primera y le damos send
y nos regresamos en la segunda peticion y vemos esto
![Pasted_image_20250829212755.png](/Imagenes/Pasted_image_20250829212755.png)
tal que queda asi
![Pasted_image_20250829212903.png](/Imagenes/Pasted_image_20250829212903.png)
nos regresamos a la primera y le damos a send
![Pasted_image_20250829212933.png](/Imagenes/Pasted_image_20250829212933.png)
y hemos logrado
