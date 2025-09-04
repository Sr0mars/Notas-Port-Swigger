En este laboratorio se explota una vulnerabilidad de tipo web cache poisoning. La clave está en que los parámetros de la URL no forman parte de la clave que usa la caché para distinguir entre distintas peticiones, lo que permite que una respuesta generada con un parámetro malicioso se almacene y luego se sirva a otros usuarios aunque accedan sin ese parámetro.

El proceso consiste en añadir un parámetro con un valor que se refleje en la respuesta y permita inyectar código malicioso. Se usa una cabecera como Origin para forzar una respuesta no cacheada, y se comprueba que el contenido malicioso queda guardado. Después se accede sin el parámetro, y si el contenido sigue presente, significa que la caché fue envenenada. El laboratorio se resuelve cuando el usuario víctima accede a la página y se ejecuta el contenido inyectado.

Solucion
seguimos los mismo pasos que anterior mente pero en este laboratorio
se aplica una injeccion en la url
![Pasted image 20250821215156.png](imagenes/Pasted image 20250821215156.png)
recargamos la pagina y aqui el resultado
![Pasted image 20250821215137.png](imagenes/Pasted image 20250821215137.png)esto por que ?
### 1. `GET`

Es el método HTTP. Aquí estás diciendo: “haz una petición GET” (es decir, solicita un recurso al servidor).

---

### 2. `/`

Indica la ruta. En este caso es `/` (la raíz del sitio).

---

### 3. `?evil=1'/><script>alert(1)</script>`

Esto es la **query string** que se envía en la URL.

- `evil` → es el nombre del parámetro.
    
- `1'/><script>alert(1)</script>` → es el valor del parámetro.
    

Lo interesante aquí es que no es un valor “normal”, sino que alguien lo armó para **inyectar código JavaScript**:

- `1'/>` → intenta **romper la estructura HTML** (cerrar un atributo o etiqueta).
    
- `<script>alert(1)</script>` → código **XSS (Cross-Site Scripting)**: abre una alerta en el navegador si llega a ejecutarse.
    

---

### 4. `HTTP/2`

Indica que la petición se está enviando usando **HTTP/2** como protocolo.

### En resumen

Funcionó porque la aplicación **no sanitizó tu input antes de meterlo en un atributo HTML**, y eso permitió:

- Salirte del `href`,
    
- Cerrar la etiqueta `<link>`,
    
- Inyectar tu propio `<script>`.
    

Eso es **XSS reflejado por inyección en atributo**.