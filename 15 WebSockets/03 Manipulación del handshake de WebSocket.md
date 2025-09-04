Este laboratorio presenta un escenario en el que una tienda online utiliza WebSockets para su sistema de chat en tiempo real. Sin embargo, la implementación contiene una lógica de filtrado de XSS defectuosa que puede ser sorteada con técnicas de evasión.

Durante la interacción con el chat, se descubre que al enviar una carga maliciosa clásica, la conexión WebSocket se termina inmediatamente y el servidor bloquea la IP del cliente. Sin embargo, este mecanismo puede ser eludido modificando la cabecera del handshake para falsificar la dirección IP mediante un encabezado específico.

Una vez restablecida la conexión usando esta técnica, se puede enviar una versión ofuscada de una carga XSS que pasa por alto el filtro del servidor. Dicha carga es ejecutada por el navegador del agente de soporte, resolviendo así el laboratorio al provocar la ejecución de un ‘**alert()**‘.

Este ejercicio demuestra cómo una mala validación en el establecimiento de conexiones WebSocket puede ser explotada para evadir mecanismos de protección y ejecutar ataques del lado del cliente.

Solucion
si nosotros intentamos hacer un ataque nos pondra en una lista negra
![Pasted_image_20250821003111.png](Imagenes/Pasted_image_20250821003111.png)
![Pasted_image_20250821003129.png](Imagenes/Pasted_image_20250821003129.png)
![Pasted_image_20250821003159.png](Imagenes/Pasted_image_20250821003159.png)
esto lo vamos a interceptar
y vamos a crear una nueva regla en settings
![Pasted_image_20250821003808.png](Imagenes/Pasted_image_20250821003808.png)
tal que quede asi
![Pasted_image_20250821003915.png](Imagenes/Pasted_image_20250821003915.png)
e interceptamos y lo dejamos fluir tal que ya se me queda la cabecera
![Pasted_image_20250821004035.png](Imagenes/Pasted_image_20250821004035.png)
ahora desde el webscokets mandamos una peticion al repeter y ejecutamos el codigo
![Pasted_image_20250821004344.png](Imagenes/Pasted_image_20250821004344.png)
![Pasted_image_20250821004359.png](Imagenes/Pasted_image_20250821004359.png)
