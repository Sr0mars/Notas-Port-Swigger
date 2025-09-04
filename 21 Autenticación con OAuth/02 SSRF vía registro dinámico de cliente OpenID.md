En esta clase se explora una vulnerabilidad de tipo Server-Side Request Forgery (SSRF) que se origina en una función legítima del estándar OpenID: el registro dinámico de clientes.

El servidor OAuth permite que nuevas aplicaciones cliente se registren automáticamente a través de un endpoint sin autenticación (/reg). Durante este proceso, el cliente puede proporcionar una propiedad opcional llamada logo_uri, que supuestamente contiene la URL del logo de la aplicación. Esta URL es posteriormente utilizada por el servidor para renderizar interfaces de autorización.

El fallo reside en que el servidor OAuth no valida adecuadamente la URL proporcionada en **logo_uri**, y realiza una petición directa a dicha URL cuando un usuario accede a la página de autorización (**/client/CLIENT-ID/logo**).

El atacante aprovecha esto para registrar una aplicación maliciosa con una logo_uri apuntando a una dirección IP reservada del proveedor cloud (169.254.169.254), que expone información sensible como las credenciales de IAM de la máquina.

Mediante este bypass, el atacante logra que el servidor realice una petición SSRF a:

- http://169.254.169.254/latest/meta-data/iam/security-credentials/admin/

Posteriormente, tras acceder al logo asociado a su aplicación, el servidor le devuelve en la respuesta las claves de acceso del entorno cloud del proveedor.

Este laboratorio demuestra cómo una simple propiedad como **logo_uri**, combinada con una validación débil, puede convertirse en una puerta de entrada hacia infraestructura crítica.

Importante Leer: (https://portswigger.net/web-security/oauth#what-is-oauth)

Solucion
![Pasted image 20250829235349.png](imagenes/Pasted image 20250829235349.png)
hacemos el mismo proceso de login y podemos ver que en el historico tenemos una peticion GET de authentification vamos a copiar el link
![Pasted image 20250829235823.png](imagenes/Pasted image 20250829235823.png)
nos sale esto 
![Pasted image 20250829235915.png](imagenes/Pasted image 20250829235915.png)
pero en la pagina de PS nos comparten una Post en el cual dice que hay rutas que nos pueden dar info
![Pasted image 20250830000149.png](imagenes/Pasted image 20250830000149.png)
vamos a copiarlo y pegarlo en la url de hace rato
y nos da info de varios endpoints
![Pasted image 20250830000328.png](imagenes/Pasted image 20250830000328.png)
y bueno vamos a darle click a una de estas que nos lleve a la raiz de es misma direccion
y esta misma la mandamos al repeater y cambiamos el metodo a post
![Pasted image 20250830000933.png](imagenes/Pasted image 20250830000933.png)
una vez cambiamos de metodo modificamos
![Pasted image 20250830001050.png](imagenes/Pasted image 20250830001050.png)
en este caso le agregamos el post el reg que tenia y era importante
![Pasted image 20250830001152.png](imagenes/Pasted image 20250830001152.png)
y vemos que nos a creado algo y vemos varios campos 
entonces nos comparten una direccion la cual supuestamente nos da informacion
tal que se veria asi y en efecto nos da un client id
![Pasted image 20250830001809.png](imagenes/Pasted image 20250830001809.png)
ese client id donde lo podemos pegar?
bueno si vemos en el historico podemos ver que en una de la peticiones get exite una validacion de cliente de un logo
![Pasted image 20250830001929.png](imagenes/Pasted image 20250830001929.png)
esto lo mandamos al repeater y modificamos ese client
ese no era era este
![Pasted image 20250830002034.png](imagenes/Pasted image 20250830002034.png)
Le damos a send y vemos que nos entrega un secret key
![Pasted image 20250830002123.png](imagenes/Pasted image 20250830002123.png)
ya solo lo copiamos y pegamos en el lab
![Pasted image 20250830002202.png](imagenes/Pasted image 20250830002202.png)

