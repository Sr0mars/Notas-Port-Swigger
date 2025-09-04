Esta clase cierra el laboratorio iniciado previamente, donde ejecutamos un XSS reflejado que evade una política CSP estricta mediante un ataque de marcado colgante. En la primera parte logramos exfiltrar el token CSRF de la víctima aprovechando la redirección y ejecución controlada de scripts.

Ahora, con el token en nuestro poder, completamos la explotación preparando un ataque CSRF dirigido. Usamos las herramientas de Burp Suite para generar automáticamente el formulario necesario, insertamos el token robado y activamos el envío automático mediante un script embebido. Este formulario, una vez cargado por la víctima, realiza una petición autenticada que modifica su dirección de correo a hacker@evil-user.net.

La clave aquí está en que todo el proceso ocurre sin interacción directa por parte de la víctima más allá de hacer clic en el enlace. Esto demuestra cómo un XSS bien planteado no solo puede ejecutar código, sino también forzar acciones dentro del flujo legítimo de una sesión activa, incluso con medidas como CSP y validación de tokens.

Este cierre consolida los conocimientos necesarios para entender cómo combinar distintas técnicas —XSS, evasión de políticas de seguridad y automatización de ataques CSRF— para lograr una explotación completa en aplicaciones reales.

