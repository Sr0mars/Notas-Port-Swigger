En esta clase explotamos una funcionalidad vulnerable al CSRF que, a pesar de usar cookies con SameSite Strict, permite el ataque debido a una redirección cliente-side basada en parámetros manipulables.

El flujo del ataque es el siguiente:

- El navegador de la víctima primero realiza una petición GET a una ruta aparentemente inocua.
- Esa ruta incluye un parámetro que se inyecta directamente en el path de redirección usando JavaScript cliente-side.
- Con esa redirección controlada, conseguimos que el navegador envíe una petición GET autenticada al endpoint de cambio de email, el cual no exige tokens y permite método GET.

Esta técnica permite bypassear SameSite Strict, ya que la cookie de sesión se envía en la segunda petición, que es una navegación directa dentro del mismo dominio. Así conseguimos que el cambio de email se efectúe sin interacción directa del usuario.

Una clase muy potente para entender cómo pequeños detalles en la lógica del frontend pueden romper protecciones modernas como SameSite.

Solucion
basicamente como tenemos una restriccion lo ideal es redirigirlo pero para esto obtenemos un script
<script>
    document.location = "https://0a7c008e04978ebc80bb26d400fd003e.web-security-academy.net/post/comment/confirmation?postId=1/../../my-account/change-email?email=pwned%40web-security-academy.net%26submit=1";
</script>
