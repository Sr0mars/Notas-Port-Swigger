En esta clase llevamos a cabo un ataque avanzado de web cache deception combinado con HTTP request smuggling. Manipulamos una petición para hacer que la solicitud de /my-account del usuario víctima quede almacenada en la caché del servidor, exponiendo así su API Key.

Una vez envenenada la caché, accedemos al contenido como si fuera un recurso estático. Este ataque requiere paciencia y repetición para sincronizarse correctamente con el acceso del usuario víctima.

Solucion
entonces lo primero es logearnos y despues vamos a interceptar lagun recurso buscando en la pagina pues nos fijamos en el resources
![[Pasted image 20250810201559.png]]
ahora vamos a interceptar con esa direccion
![[Pasted image 20250810201804.png]]
que significa esto que esta configuracion va ser nuestro cache poison (aqui solamente le dimos el http1.1)
lo siguiente sera capturar un intercepcion normal
y configurarlo hacia my acount para obtner la apikey
![[Pasted image 20250810202320.png]]
Entonces nosotro buscamos el error 302 para que asi verificar en la otra pagina cacheada el apikey del administrador
![[Pasted image 20250810203659.png]]
de esta forma ya obtenemos el api key del administrador desde la otra pagina cacheada
![[Pasted image 20250810203825.png]]

