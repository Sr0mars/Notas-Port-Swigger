En esta clase resolvemos un caso de SSRF donde el stock **checker** sólo permite acceder a rutas internas de la propia aplicación, bloqueando directamente URLs externas. Sin embargo, identificamos una vulnerabilidad de redirección abierta en el parámetro path del endpoint ‘nextProduct’.

Aprovechamos esta redirección para hacer que el stock checker acceda de forma indirecta al panel de administración interno ubicado en http://192.168.0.12:8080/admin. Desde ahí, utilizamos la misma técnica para construir una URL que elimine al usuario carlos, completando así el laboratorio. Este enfoque muestra cómo una redirección abierta puede ser encadenada con un SSRF para saltarse restricciones de filtrado.

Solucion
De igual manera vamos a interceptar el check stock
y bueno aqui nosotros no tenemos acceso al localhost por lo cual no tenemos ni domios ni subdominos
![Pasted_image_20250804201223.png](/Imagenes/Pasted_image_20250804201223.png)
pero si notros vemos tenemos una opcion de next product la cual me lleva hacia otra otro producto pero contenpla el path
![Pasted_image_20250804201558.png](/Imagenes/Pasted_image_20250804201558.png)
asi que si le damos click derecho y copiamos el link nosotros podemos redirigirlo hacia el servidor tercero en donde se encuentra la pagina
![Pasted_image_20250804201957.png](/Imagenes/Pasted_image_20250804201957.png)
https://0a210045039739cc8215387a00360045.web-security-academy.net/product/nextProduct?currentProductId=1&path=/product?productId=2

asi que  nosotros contemplanos en donde empieza el path para poder redirigir
![Pasted_image_20250804202544.png](/Imagenes/Pasted_image_20250804202544.png)
y ya solo seria poder eliminar el usuario carlos con la url
![Pasted_image_20250804202717.png](/Imagenes/Pasted_image_20250804202717.png)

