En esta segunda clase, se audita la aplicación en busca de rutas que puedan actuar como proxy o facilitar la fuga de información. Se analiza la página /post/comment/comment-form, la cual está embebida en las entradas del blog mediante un iframe.

Este formulario contiene un comportamiento inseguro: utiliza ‘**window.postMessage()**‘ para enviar la URL actual (**window.location.href**) al parent window, sin restringir el origen de destino (**targetOrigin: ‘*’**). Esto significa que cualquier página que lo cargue en un iframe podrá recibir esa información, incluida la fragmentación de la URL donde se encuentra el token de acceso.

Este comportamiento convierte al formulario de comentarios en una herramienta perfecta para recolectar el token que se inyectará en la tercera clase.

Solucion
verificamos que es lo que hace el script del historico
![Pasted_image_20250830193701.png](/Imagenes/Pasted_image_20250830193701.png)
Que hace ?
Este script se utiliza para comunicar información desde un iframe hacia su página padre (es decir, el documento que contiene el iframe). Envía datos cuando la página se carga y cuando se envía un formulario.
ejemplo
![Pasted_image_20250830193818.png](/Imagenes/Pasted_image_20250830193818.png)
