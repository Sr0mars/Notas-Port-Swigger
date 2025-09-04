En esta clase se aborda una vulnerabilidad Server-Side Request Forgery (SSRF) derivada del uso inseguro de la cabecera Host como criterio de enrutamiento interno.

El laboratorio presenta una aplicación que redirige el tráfico en función del valor de la cabecera Host. Mediante Burp Collaborator, comprobamos que la aplicación es capaz de emitir peticiones externas basadas en el valor de Host, lo que demuestra una clara exposición SSRF.

Utilizando Burp Intruder, realizamos un ataque por fuerza bruta sobre la cabecera Host, explorando toda la subred 192.168.0.0/24. Uno de los valores devuelve un 302 hacia /admin, indicando que hemos accedido al panel interno. A partir de ahí, inspeccionamos el panel para capturar el token CSRF y la cookie de sesión, y construimos manualmente una petición POST a /admin/delete, incluyendo el token y el nombre de usuario carlos como parámetros.

Esta clase enseña cómo una mala gestión del enrutamiento basado en cabeceras puede permitir a un atacante interactuar con sistemas internos no expuestos directamente, violando el modelo de confianza de la red interna.

Solucion
