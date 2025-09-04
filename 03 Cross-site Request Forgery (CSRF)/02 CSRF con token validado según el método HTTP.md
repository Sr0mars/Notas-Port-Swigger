En esta clase pasamos a un escenario de CSRF con validación parcial, donde la aplicación implementa una defensa basada en tokens pero solo la aplica cuando la petición utiliza el método POST. Si el mismo endpoint es accedido mediante GET, la validación del token queda desactivada.

Aprovechamos esta inconsistencia cambiando el método de la solicitud de POST a GET. De este modo, no es necesario incluir un token válido, y la petición de cambio de correo electrónico es aceptada siempre que el usuario esté autenticado.

Utilizamos un formulario HTML alojado en el servidor de explotación, que se autoenvía al cargarse y realiza una petición GET con los parámetros necesarios. Como el servidor no exige el token en este contexto, la modificación se lleva a cabo con éxito, demostrando que el control de CSRF es incompleto.

Este laboratorio pone de relieve un error común en la implementación de defensas: aplicar la validación solo en ciertos métodos sin limitar realmente qué métodos están permitidos en el endpoint. Es un paso más en la evolución del ataque CSRF hacia entornos parcialmente protegidos.

Solucion
otra vez tenemos que poner una pagina fraudulenta
lo primero seria cambiar nuestro correo pero para ello vamos a interceptarlo con BS y esto lo mandamos al repeater
asi que podemos ver que tenemos un csrf le damos CTRL+SHIFT+U

![[Pasted image 20250722174024.png]]

y lo que podemos hacer es mandarlo por GET ya que actualmente se esta pasando por post para ello damos click derecho y le cambiamos el metodo (esto solo es para comprobar)
![[Pasted image 20250722174955.png]]

lo comprobamos con cambiarle el nombre del correo y ver el esta que es 302
![[Pasted image 20250722175246.png]]
pero esto lo podemos comprobar dandole follow redirec
![[Pasted image 20250722175402.png]]
entonces con esto corroboramos que esta en funcionamiento por lo cual podemos hacer es que copiamos el codigo del formulario le damos click derecho y editar html

"
<form class="login-form" name="change-email-form" action="https://0a4d00880366100380e603ee00cb0090.web-security-academy.net/my-account/change-email" method="GET">
    <input type="hidden" name="email" value="pwned@pwned.com">
</form>

<script>
        document.forms[0].submit();
</script>
"
esto se hace por que el csrf no lo pide
