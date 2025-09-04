En esta clase ponemos en práctica un caso realista de XSS almacenado con robo de sesión, donde el código malicioso se inyecta en un comentario de blog y se activa cuando otro usuario —en este caso, una víctima simulada— visualiza la página.

Aprovechamos la vulnerabilidad para insertar un fragmento de código que, al ejecutarse en el navegador de la víctima, recopila su cookie de sesión y la envía en segundo plano a un servidor externo controlado a través de Burp Collaborator, una herramienta diseñada para capturar interacciones fuera de banda.

Una vez interceptada la cookie, la utilizamos para suplantar la identidad del usuario afectado, inyectándola en nuestras propias peticiones mediante un proxy o el módulo Repeater de Burp Suite. Esto nos da acceso a áreas privadas como si fuéramos la víctima.

Este laboratorio demuestra cómo un XSS puede ir más allá de una simple alerta visual y usarse para comprometer directamente cuentas de usuario, lo que lo convierte en uno de los vectores más críticos en seguridad web.

