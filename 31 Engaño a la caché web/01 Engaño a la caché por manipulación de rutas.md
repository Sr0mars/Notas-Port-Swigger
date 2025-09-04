En esta clase descubrimos cómo algunas rutas dinámicas, como ‘**/my-account**‘, siguen funcionando incluso si se les añade una extensión como ‘**.js**‘. El servidor las interpreta correctamente, pero la caché las trata como contenido estático y almacena la respuesta. Aprovechamos esto para forzar a la víctima (carlos) a acceder a una ruta modificada que luego cacheamos con su información, permitiéndonos recuperar su clave API desde el navegador.

Solucion
![[Pasted image 20250902125916.png]]
![[Pasted image 20250902130027.png]]
La web:
![[Pasted image 20250902130204.png]]
nos comparten un exploit server nos logeamos
![[Pasted image 20250902130244.png]]
vamos a interceptar esto y lo mandamos al repeater
![[Pasted image 20250902130321.png]]
si nosotro pasamos a pones cualquiero cosa en le get vemos que nos lo sigue interprentando
![[Pasted image 20250902130426.png]]
de igual forma si ponemos una extencion
![[Pasted image 20250902130700.png]]
vemos que se reinicia la cache lo cual juega a favor de nosotros
asi que algo que podemos hacer en el exploit server es esto
![[Pasted image 20250902130741.png]]
nota: me falto poner el ; alfinal del las comillas
ahora si visitamos la url con la extencion my-account/ejemplo.js
podemos ver que nos entrega la apy key de carlos
![[Pasted image 20250902131012.png]]
![[Pasted image 20250902131123.png]]
