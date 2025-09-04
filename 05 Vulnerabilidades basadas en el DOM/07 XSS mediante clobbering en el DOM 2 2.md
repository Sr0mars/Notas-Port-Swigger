En esta segunda parte se ve cómo, tras realizar la inyección inicial de elementos malformados en los comentarios del blog (los que clobberizan la variable esperada por el script), la manipulación persiste en el DOM del navegador y se reactiva automáticamente al interactuar de nuevo con la página.

Cuando se carga el mismo post por segunda vez o se añade un nuevo comentario, el script incluido en la página intenta acceder a la variable global que fue clobberizada. Como esta variable ahora contiene un valor malicioso con una ruta construida a partir del protocolo ‘**cid:**‘ y un evento ‘**onerror**‘, se desencadena la ejecución del código JavaScript embebido.

Esto demuestra cómo es posible introducir un estado alterado en la estructura de la aplicación que será explotado más adelante sin necesidad de interacción directa con el usuario. La ejecución no ocurre en el momento del primer comentario, sino al volver a procesar esa variable manipulada, lo cual da una idea de cómo funciona la persistencia del clobbering en combinación con scripts mal diseñados.

Este ejemplo sirve como advertencia sobre el uso de patrones de inicialización peligrosos y la importancia de validar los nodos del DOM antes de utilizarlos como estructuras de datos.

Solucion
Viendo el codigo fuente checamos esto
![[Pasted image 20250727212002.png]]
Este código HTML está diseñado como un **payload de DOM Clobbering para provocar un XSS indirecto**. Se basa en que un script vulnerable utilice `document.avatar.href` (esperando que `avatar` sea un objeto `img` o `a` legítimo), pero el atacante inyecta su propio `<a name="avatar">` con un `href` malicioso que termina inyectando un evento `onerror` en un contexto HTML.
y bueno para esto aplicamos este payload
(<a id=defaultAvatar>
<a id=defaultAvatar name=avatar href="cid:&quot;onerror=alert(0)>//">)
Este payload explota una combinación de:

- **DOM Clobbering** con `name="avatar"` → `document.avatar`
    
- **Malformación de `href`** para inyectar un atributo `onerror` y ejecutar `alert(0)`
    
- **Uso potencialmente inseguro de `.href` en scripts**
    

👉 Por sí solo no hace daño, pero en una aplicación vulnerable puede permitir **ejecución arbitraria de JavaScript (XSS)**.


![[Pasted image 20250727213522.png]]

