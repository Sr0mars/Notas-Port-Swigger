En este laboratorio aprovechamos una vulnerabilidad de tipo DOM XSS donde la aplicación recibe mensajes mediante postMessage, los interpreta como JSON con JSON.parse y, según su contenido, modifica dinámicamente el atributo src de un iframe interno.

El ataque consiste en enviar desde un iframe un mensaje JSON con un campo type establecido en load-channel y un campo url que contiene un payload en forma de URL JavaScript. El listener interno interpreta el mensaje, valida el tipo y actualiza el iframe sin realizar ninguna comprobación de origen ni sanitización.

El resultado es la ejecución directa de la función print en el navegador de la víctima, demostrando cómo la falta de validación y confianza ciega en los datos recibidos puede derivar en una ejecución remota de código.

Solucion
De nuevo realizamos la busquedad en la pagina fuente para ver que hay
![Pasted_image_20250727171017.png](/Imagenes/Pasted_image_20250727171017.png)
Codigo fuente
![Pasted_image_20250727171058.png](/Imagenes/Pasted_image_20250727171058.png)
Este script:

- Escucha mensajes `postMessage` en formato JSON.
    
- Crea y controla un `iframe` dentro del documento según el tipo de mensaje recibido.
    
- Permite cargar contenido dinámico y ajustar el tamaño del reproductor ("ACMEplayer").
    
- **Es vulnerable si no se restringe el origen ni se validan las URLs**.

**Procesa el mensaje según su tipo (`d.type`)**:

- `"page-load"`: hace que el iframe se desplace a la vista (`scrollIntoView()`).
    
- `"load-channel"`: cambia la URL del iframe (`iframe.src = d.url`).
    
- `"player-height-changed"`: ajusta el tamaño del iframe.

Entonces el campo donde es vulnerable es el de load-channel
![Pasted_image_20250727173127.png](/Imagenes/Pasted_image_20250727173127.png)
por lo cual esto ahora deberemos pasarlo al payload
(<iframe src=https://0af80029030fc2d380427b23000e00e1.web-security-academy.net/ onload='this.contentWindow.postMessage("{\"type\":\"load-channel\",\"url\":\"javascript:print()\"}","*")'>)
Este payload intenta **abusar de un script en el sitio víctima** que:

- Recibe datos por `postMessage`.
    
- Usa `JSON.parse`.
    
- Crea un `iframe` con `src = d.url` sin validación.
    
- Permite esquemas como `javascript:` en la URL.
    

Si el sitio es vulnerable, el payload logra **ejecutar JavaScript arbitrario en el navegador de la víctima**, lo que equivale a **XSS remoto**.

