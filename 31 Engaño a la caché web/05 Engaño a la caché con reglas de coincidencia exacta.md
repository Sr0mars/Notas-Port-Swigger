En esta clase descubrimos cómo el servidor cachea archivos estáticos como robots.txt siguiendo una regla de coincidencia exacta. Aprovechamos un error en la normalización de rutas, donde la caché interpreta secuencias como ‘**;%2f..%2frobots.txt**‘ como equivalentes a ‘**/robots.txt**‘, permitiendo que se almacene una versión cacheada de otra ruta.

Usamos este truco para extraer el token CSRF del administrador, y con él, construimos un ataque CSRF que nos permite modificar su dirección de correo electrónico, resolviendo así el laboratorio.

Solucion
nos logeamos pero ahora no nos dan ningun api key vamos a interceptar el cambio de correo 
![[Pasted image 20250902140218.png]]
y a esto mismo le hacemos un drop
![[Pasted image 20250902140354.png]]
![[Pasted image 20250902140420.png]]
y ahora vamos a interceptar una solicitud get en la misma parte
![[Pasted image 20250902140710.png]]
y la peticion get probamos los delimitadores que antes estabamos probando
![[Pasted image 20250902140817.png]]
asi que esto lo mandamos al intruder
obtenemos el ? y el ;
![[Pasted image 20250902140854.png]]

si nos vamos al historico vemos de nuevo que se aplica al directorio resources
![[Pasted image 20250902141200.png]]
sin embargo no nos da la cache
algo que podemos hacer es aprovechar de la ruta robots.txt
![[Pasted image 20250902141541.png]]
y vamos probando con los delimitadores
hasque no nos de respuesta de cache y alfin encontramos uno
![[Pasted image 20250902141750.png]]
y en el exploit server quedaria algo asi
![[Pasted image 20250902142033.png]]
y nos vamos al repeater y nos sale esto
![[Pasted image 20250902142128.png]]
copiamos el csrf token de aqui
lo pegamos en el change email click derecho generate CSRF Poc
![[Pasted image 20250902143437.png]]
lo copiamos en el exploit
![[Pasted image 20250902143524.png]]
y store
<!DOCTYPE html>
<html lang="en">
	<body>
		<h1>Form CSRF PoC</h1>
		<form method="POST" action="https://undefined/my-account/change-email">
			<input type="hidden" name="Host: 0a3800c7049f3c3482bc9c7a00a7003e.web-security-academy.net" value="">
			<input type="submit" value="Submit Request">
		</form>
	</body>
</html>

