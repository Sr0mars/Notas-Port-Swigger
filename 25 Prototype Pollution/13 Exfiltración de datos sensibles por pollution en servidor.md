En esta clase explotamos una vulnerabilidad crítica de server-side prototype pollution en una aplicación Node.js, que permite modificar el comportamiento interno del servidor y ejecutar comandos arbitrarios. A través de una funcionalidad legítima de cambio de dirección, inyectamos propiedades maliciosas dentro de ‘**proto**‘, aprovechando un gadget que ejecuta procesos secundarios.

Utilizamos campos como ‘**shell**‘ e ‘**input**‘ para lanzar comandos a través de vim en modo no interactivo, y redirigimos la salida de comandos como ‘**ls**‘ y ‘**cat**‘ codificados en base64 hacia un servidor controlado mediante Burp Collaborator. Primero listamos el contenido del directorio ‘**/home/carlos**‘, y después exfiltramos el contenido del archivo ‘**secret**‘.

Esta clase demuestra cómo una combinación de contaminación del prototipo y ejecución de comandos puede llevar a la filtración de datos sensibles incluso sin necesidad de acceso físico al sistema.

Solucion
nos logeamos e interceptamos y lo mandamos al repeater

vemos si es vulnerable ,"__proto__":{"json spaces":10}


