En esta primera parte, analizamos cómo el servidor front-end es vulnerable a HTTP/2 request tunnelling a través de la inyección de caracteres de nueva línea (\r\n) en los nombres de cabecera. Verificamos que podemos inyectar cabeceras arbitrarias, como Host, lo que nos permite comenzar a manipular la interpretación del servidor.

Esta prueba inicial demuestra que la infraestructura permite colapsar cabeceras a nivel HTTP/1.1 tras el downgrade desde HTTP/2, clave para las siguientes fases del ataque

Solucion
Vamos a interceptar pagina home pero en este caso no cambiaremos nada por que no es vulnerable a todas las pruebas que hemos hecho anteriormente asi que en esta ocacion vamos a probar poner una cabecera pero en el apartado de name para ver si es vulnerable
![[Pasted image 20250811165856.png]]
Le damos al add seguido de send y notamos un error
![[Pasted image 20250811170021.png]]
por lo cual nosotros podemos agregar una cabecera