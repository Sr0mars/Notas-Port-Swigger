En este laboratorio nos encontramos con una implementación de tokens CSRF que no están vinculados a la sesión del usuario. Esto significa que cualquier token válido puede ser utilizado por cualquier usuario, sin importar quién lo haya recibido originalmente.

Para explotar esta debilidad:

- Iniciamos sesión con un usuario y capturamos un token CSRF desde la funcionalidad de cambio de correo electrónico.
- Luego, iniciamos sesión con otro usuario y utilizamos ese token previamente obtenido para enviar una solicitud de cambio de correo.
- El servidor acepta el token aunque no pertenezca a esa sesión, lo que permite realizar el ataque CSRF.

Esta vulnerabilidad demuestra la importancia de vincular los tokens CSRF al contexto de la sesión del usuario que los recibió, de lo contrario, pueden ser reutilizados de forma maliciosa.

Solucion
lo primero seria interceptar el cambio de correo por BS por lo que ahora los tokens son unicos
![[Pasted image 20250722215152.png]]

sin encambio podemos cambiarlo por medio de carlos que es el otro correo que nos dieron
![[Pasted image 20250722215609.png]]
(pero antes vamos a instalar una extenxion llamada notes)
por lo cual en las notas vamos a copiarnos el CSRF TOKEN  y luego le vamos a dar drop para eliminar la solicitud
![[Pasted image 20250722215816.png]]
le damos en drop en el proxy le de damos intercept off
![[Pasted image 20250722215937.png]]
por lo cual ahora pasamos a cambiarle el correo nuevamente
entonces desde el historial buscamos la primerita csrf que pusimos y esto lo mandamos al repeater
![[Pasted image 20250722220454.png]]
asi que desde el reapaeter cambiamos el correo y no lo ponemos el csrf token de carlos le damos send
![[Pasted image 20250722220710.png]]

asi que lo que podemos hacer es primero no vamos al usuario wiener y nos cambiamos el correo y vamos a interceptarlo
me copio el csrf token
![[Pasted image 20250722221101.png]]
ahora dejamos de interceptar y vamos a copiarnos la plantilla para crear el script
![[Pasted image 20250722221631.png]]
Basicamente lo que hacemos aqui es suplantar el antiguo CSRF por el que copiamos anteriormente para que con esto nos de entrada al cambio de correo

<form class="login-form" name="change-email-form" action="https://0a4700c703792b9e805a354800920091.web-security-academy.net/my-account/change-email" method="POST">
    <input type="hidden" name="email" value="se@tenso.com">
    <input required="" type="hidden" name="csrf" value="QUAQNuWkPQZwhhcos5kUFzZGpi3Yte0n">
</form>

<script>
    document.forms[0].submit();
</script>




