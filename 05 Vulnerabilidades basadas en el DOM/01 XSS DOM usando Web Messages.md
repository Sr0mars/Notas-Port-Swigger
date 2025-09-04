Este laboratorio demuestra cómo una vulnerabilidad DOM XSS puede explotarse a través del uso de web messages. La página objetivo escucha mensajes entrantes con addEventListener y luego inserta su contenido directamente en el DOM dentro de un contenedor específico, sin ningún tipo de validación.

Desde el servidor de explotación, se carga la página vulnerable dentro de un iframe y se utiliza postMessage para enviar un payload malicioso que contiene una etiqueta img con un atributo onerror que ejecuta la función print. Esta acción demuestra cómo el uso inseguro de web messages puede comprometer la seguridad del sitio cuando el contenido recibido se trata como si fuera seguro.

Solucion
Como sabemos en el caso del xss se tiene que checar en todas partes y en este caso verificamos el codigo fuente siempre buscando el script
La pagina web
![Pasted_image_20250727162908.png](/Imagenes/Pasted_image_20250727162908.png)
El codigo fuente
![Pasted_image_20250727162936.png](/Imagenes/Pasted_image_20250727162936.png)
### Explicación:

1. **`window.addEventListener('message', ...)`**  
    Este código añade un _escuchador de eventos_ al objeto `window` para el evento `'message'`.  
    Ese evento se dispara cuando otra ventana (como un iframe, popup o ventana externa) envía un mensaje usando `window.postMessage()`.
    
2. **`function(e) { ... }`**  
    Define una función que se ejecutará cada vez que se reciba un mensaje.  
    El parámetro `e` representa el evento, y `e.data` contiene el mensaje que fue enviado.
    
3. **`document.getElementById('ads').innerHTML = e.data;`**  
    Toma el contenido del mensaje (`e.data`) y lo inserta como HTML dentro del elemento con `id="ads"`.
    

---

### ¿Qué efectos tiene esto?

- Permite a tu página recibir contenido dinámico desde otro origen (por ejemplo, un iframe externo con anuncios).
    
- Ese contenido recibido se inserta directamente en el DOM (en el elemento con ID `"ads"`).
    
- **Importante**: esto puede ser riesgoso si no se valida el origen del mensaje (`e.origin`), porque podría permitir _Cross-Site Scripting (XSS)_ si alguien malicioso envía código HTML o JavaScript.

Lo cual nos podemos aprovechar
de esta manera
![Pasted_image_20250727163556.png](/Imagenes/Pasted_image_20250727163556.png)
pero esto lo tendremos que hacerlo en payload 
(<iframe src="https://0a92007a042f59288084039d00b9004d.web-security-academy.net/" onload="this.contentWindow.postMessage('<img src=1 onerror=print()>','*')">)

Este payload intenta **inyectar y ejecutar JavaScript malicioso en una página vulnerable** que usa `window.postMessage` y `innerHTML` sin validar el origen del mensaje ni sanitizar el contenido. Es una técnica común en retos de seguridad y ataques XSS modernos.

