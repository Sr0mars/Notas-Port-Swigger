En este laboratorio explotamos una vulnerabilidad de tipo DOM XSS basada en redirección, donde la aplicación escucha mensajes entrantes mediante postMessage y utiliza su contenido como destino para un cambio de página usando ‘**location.href**‘. Aunque intenta validar que la URL comienza con http o https, el uso incorrecto de indexOf permite eludir la comprobación.

Desde el exploit server, se carga la página vulnerable dentro de un iframe y se envía un mensaje que contiene un payload JavaScript válido seguido de una cadena que incluye http, lo suficiente para pasar el filtro. Al llegar al sink ‘**location.href**‘, se ejecuta la función print, demostrando cómo una validación mal implementada puede abrir la puerta a la ejecución de código arbitrario.

Solucion 
Un poco igual que el anterior laboratorio toca revisar el codigo fuente
![Pasted_image_20250727164851.png](Imagenes/Pasted_image_20250727164851.png)
Codigo Fuente
![Pasted_image_20250727164910.png](Imagenes/Pasted_image_20250727164910.png)
Este script permite **redireccionar el navegador a una URL externa mediante un mensaje postMessage**. Sin validación del origen, es **una vulnerabilidad seria** que puede ser explotada para ataques de phishing, redirección maliciosa o robo de usuarios.
por lo cual esto se ve reflejado de esta manera
![Pasted_image_20250727165902.png](Imagenes/Pasted_image_20250727165902.png)
ahora tocaria pasarlo a payload
(<iframe src="https://0a4d00e903ba3cbe81dfa75600f0004c.web-security-academy.net/" onload="this.contentWindow.postMessage('javascript:print()//http:','*')">)
Es un intento de **ataque basado en redirección abierta (open redirect) o ejecución de JavaScript** mediante `postMessage`, aprovechando un script vulnerable que redirige usando `location.href = e.data` sin validación adecuada.
Este payload intenta **engañar a una página vulnerable** para que ejecute un `javascript:` como redirección a través de `postMessage`, lo que puede llevar a **XSS** o **ataques de redirección maliciosa**. Es una técnica común en pruebas de seguridad.


