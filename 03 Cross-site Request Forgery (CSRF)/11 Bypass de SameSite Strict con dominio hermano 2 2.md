En esta clase aprovechamos una XSS reflejada en un subdominio hermano para ejecutar un ataque de WebSocket hijacking, exfiltrando el historial de chat de la víctima.

Aunque la cookie de sesión está protegida con la directiva SameSite=Strict, el navegador la enviará si la petición proviene de un mismo sitio, como un subdominio legítimo. La XSS reflejada en cms-lab-id.web-security-academy.net se usa para inyectar un payload que abre un WebSocket al dominio principal, simula el mensaje READY y envía el contenido recibido al servidor de Burp Collaborator.

Esto demuestra cómo una XSS en un dominio hermano puede comprometer por completo la cuenta del usuario, incluso cuando se aplican protecciones modernas como SameSite Strict.


