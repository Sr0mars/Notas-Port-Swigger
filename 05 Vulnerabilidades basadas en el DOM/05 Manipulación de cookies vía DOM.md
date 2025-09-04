En este laboratorio trabajamos con una vulnerabilidad de tipo XSS basada en la manipulación de cookies mediante JavaScript en el lado del cliente. La web almacena en una cookie llamada lastViewedProduct la última URL de producto visitada, la cual es luego procesada sin validación.

El ataque consiste en forzar a la víctima a cargar una URL de producto con código malicioso embebido, lo que provoca que dicha URL sea almacenada como cookie. Justo después, la víctima es redirigida a la página de inicio. Al acceder a esa página con la cookie manipulada, se evalúa su contenido y se ejecuta el payload XSS. Con esto conseguimos que la función print() se dispare sin que el usuario sospeche nada.

Solucion
esto es un poco raro por que en este caso la injeccion se encuentra en la parte del visitar el ultimo producto
![Pasted_image_20250727175527.png](Imagenes/Pasted_image_20250727175527.png)
lo que nos da un identificador en la url
asi que en este caso vamos a interceptar un solicitud de la pagina home
![Pasted_image_20250727175815.png](Imagenes/Pasted_image_20250727175815.png)
y vemos algo raro en la intercepcion es que nos alamcena la url
![Pasted_image_20250727175758.png](Imagenes/Pasted_image_20250727175758.png)
y esto si lo vemos en el codigo fuente no lo esta metiendo todo almacena en un href
![Pasted_image_20250727180104.png](Imagenes/Pasted_image_20250727180104.png)
por lo cual podemos probar cerrar con comillas
![Pasted_image_20250727180156.png](Imagenes/Pasted_image_20250727180156.png)
pero no vemos en ningun lado la injeccion. Sin embargo si nosotros le damos en HOME veremos que ahy se encuentra
![Pasted_image_20250727180328.png](Imagenes/Pasted_image_20250727180328.png)
y esto se veria de esta forma en el codigo fuente
![Pasted_image_20250727180412.png](Imagenes/Pasted_image_20250727180412.png)
para esto hacemos el script (<iframe src="https://0a0a00270385bc8c8028032900dd00cc.web-security-academy.net/product?productId=1&'><script>print()</script>" onload="if(!window.x)this.src='https://0a0a00270385bc8c8028032900dd00cc.web-security-academy.net/';window.x=1;">)
Este payload usa un iframe para **intentar explotar una vulnerabilidad de XSS reflejado** al inyectar un `<script>` mediante un parámetro (`productId`). Si el sitio víctima refleja ese valor en el HTML sin sanitizar, se ejecutará JavaScript. El `onload` sirve para recargar o evitar bucles.


