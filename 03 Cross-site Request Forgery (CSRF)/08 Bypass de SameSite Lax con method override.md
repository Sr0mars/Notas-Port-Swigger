En esta clase explotamos una implementación vulnerable al CSRF que, a pesar de usar cookies con SameSite por defecto en modo Lax, sigue siendo atacable. La clave del ataque es que los navegadores como Chrome permiten enviar cookies ‘**SameSite=Lax**‘ en peticiones GET que implican una navegación a nivel superior.

Como la funcionalidad de cambio de email solo acepta peticiones POST, utilizamos una técnica conocida como method override, que consiste en enviar un parámetro especial (_method=POST) en la query string para que el servidor trate una petición GET como si fuera POST.

Esto nos permite construir un ataque que simplemente redirige al usuario víctima con ‘**document.location**‘ hacia una URL especialmente manipulada, logrando que su navegador envíe la cookie de sesión y realice el cambio de email sin ninguna interacción adicional.

Una clase esencial para entender cómo incluso protecciones modernas como SameSite pueden ser burladas si el backend acepta overrides de métodos.

Solucion
empezamos haciendo los mismo pasos pero a diferencia de los otros ningun CSRF
![[Pasted image 20250723212448.png]]
lo que podemos hacer es que hacer que por medio de get se haga una peticion POST poniendo de intermediario el method
eso se hace asi
le damos click derecho y change request method
![[Pasted image 20250723212921.png]]
y con esto podemos modificar para obtener el cambio de correo
![[Pasted image 20250723213228.png]]
Aqui vemos como hemos cambiado el correo
![[Pasted image 20250723213151.png]]y viendo que si funciona pasamos a realizar el payload que en esta ocacion solo vamos a redirigirlo
<script>
    document.location = "https://0a43003f0426d3ae802a124700ca00c8.web-security-academy.net/my-account/change-email?email=c@a.com&_method=POST";
</script>
