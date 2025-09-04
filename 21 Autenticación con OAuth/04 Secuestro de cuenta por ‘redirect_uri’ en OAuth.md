En esta clase se analiza un ataque de secuestro de cuenta mediante OAuth, aprovechando una mala configuración del parámetro **redirect_uri** en el servidor de autorización. El objetivo es robar el código de autorización OAuth del administrador y utilizarlo para acceder a su cuenta en la aplicación cliente.

El atacante inicia sesión normalmente a través del proveedor OAuth y observa que el código de autorización (code) es enviado como parámetro en una redirección tras la autenticación. Sin embargo, nota que puede modificar el **redirect_uri** por cualquier dominio, y el servidor OAuth lo acepta sin validación alguna. Esto le permite redirigir el código de autorización hacia un servidor controlado por él, como el exploit server.

Con esto, el atacante construye un exploit que contiene un iframe apuntando a una petición OAuth con el **redirect_uri** alterado, de forma que el código de autorización del administrador será redirigido automáticamente a su servidor. Dado que el administrador tiene una sesión activa con el proveedor OAuth, el ataque se completa sin que la víctima tenga que hacer nada más que abrir el exploit.

Una vez que el código robado aparece en los logs del exploit server, el atacante lo usa para completar manualmente el flujo de autenticación visitando la URL del callback de la aplicación con el código robado como parámetro. Esto hace que el sistema lo autentique como el administrador.

Ya con acceso a la cuenta del administrador, el atacante puede entrar al panel de administración y eliminar al usuario carlos, resolviendo así el laboratorio.

Esta clase pone en evidencia la importancia de restringir correctamente los valores aceptados en **redirect_uri**, ya que un fallo en esta validación puede llevar a comprometer cuentas críticas.

Solucion
nos logeamos como normalmente y nos vamos al historico vemos que se tramita en get una pericion que valida el uri
![Pasted_image_20250830005738.png](/Imagenes/Pasted_image_20250830005738.png)
este hace un callback asi que vamos a copiar la url de esto
asi que por medio del exploit server vamos a crear un ifram el cual nos permita obtener la peticion
![Pasted_image_20250830010327.png](/Imagenes/Pasted_image_20250830010327.png)
asi que ahora eliminamos esto y pegamos en esa misma parte nuestro exploit server url
![Pasted_image_20250830010406.png](/Imagenes/Pasted_image_20250830010406.png)
y quedaria asi
![Pasted_image_20250830010522.png](/Imagenes/Pasted_image_20250830010522.png)
en los acces log vemos que se a tramitado
![Pasted_image_20250830010726.png](/Imagenes/Pasted_image_20250830010726.png)
asi que nos copiamos este codigo 
y lo pegamos
![Pasted_image_20250830010835.png](/Imagenes/Pasted_image_20250830010835.png)
