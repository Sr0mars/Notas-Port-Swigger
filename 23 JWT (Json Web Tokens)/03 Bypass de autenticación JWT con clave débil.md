En esta clase analizamos una mala práctica común en la implementación de autenticación basada en JWT: el uso de claves de firma extremadamente débiles. Iniciamos sesión con un usuario estándar, interceptamos el token y lo sometemos a un proceso de fuerza bruta utilizando herramientas como Hashcat para descubrir la clave secreta, que resulta ser una palabra sencilla incluida en diccionarios comunes.

Una vez obtenida la clave, la usamos para firmar un token modificado en el que suplantamos al usuario administrador. Al enviar este JWT correctamente firmado, accedemos al panel de administración y eliminamos al usuario Carlos.

Este laboratorio evidencia los riesgos de usar secretos predecibles y destaca la importancia de emplear claves robustas en sistemas de autenticación basados en tokens.

Solucion
antes de empezar vamos a instalar una extencion 
![[Pasted image 20250830231951.png]]
tambien nos comparten un diccionario de contraseñas (https://github.com/wallarm/jwt-secrets/blob/master/jwt.secrets.list)
la descargamos con wget
nos logeamos y tratamos de meternos al admin interceptamos
![[Pasted image 20250830232532.png]]
ahora ya no podemos modificar el administrator por que ahora si tiene un proceso de verificacion
![[Pasted image 20250830232714.png]]
asi que vamos a aplicar BF nos copeamos toda la cookie y lo almacenamos y con hashcat y el primer diccionario que nos descargamos vamos a probar si se puede BF
![[Pasted image 20250830233021.png]]
y nos sale esto
![[Pasted image 20250830233646.png]]
ahora ya que tenemos nuestro JWT key nos vamos al BS a la extenxion y le damos new Symetric key
![[Pasted image 20250830233952.png]]
le damos a generate y la cadena que nos dio que fue secret1 vamos a pasarla por el decoder y la vamos a convertir a base64
![[Pasted image 20250830234158.png]]
tal que queda asi
![[Pasted image 20250830234257.png]]
le damos ok
y va a quedar asi
![[Pasted image 20250830234320.png]]
y nos regresamos al intercep y le damos a la pestaña de JWT
![[Pasted image 20250830234410.png]]
y ahora vamos a modificar el wiener por administrator
![[Pasted image 20250830234515.png]]
y abajo hay una opcion de sign le picamos quedaria asi
![[Pasted image 20250830234615.png]]
le damos ok y nos copiamos la nueva JWT que seria la cookie
![[Pasted image 20250830234723.png]]
pegamos y eliminamos al usuario carlos
![[Pasted image 20250830234751.png]]


