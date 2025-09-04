En esta clase de nivel experto trabajamos con un entorno protegido por una política CSP que impide la ejecución de scripts inyectados, a pesar de que existe una vulnerabilidad de XSS reflejado. El sistema refleja el contenido enviado por el usuario, pero la política de seguridad bloquea cualquier intento de ejecución directa.

La clave para resolver este laboratorio está en identificar que la cabecera CSP incluye una directiva de reporte que contiene un parámetro controlado por el usuario. Al modificar ese parámetro, es posible inyectar nuevas directivas dentro de la política CSP, lo que nos permite alterar su comportamiento desde fuera.

Utilizamos este vector para insertar una nueva directiva script-src-elem y habilitar inline scripts. Esta directiva tiene precedencia sobre la más restrictiva script-src, permitiendo la ejecución de código directamente dentro de elementos script sin necesidad de cargar archivos externos o definir hashes.

Este laboratorio demuestra cómo las políticas de seguridad mal configuradas, aunque parezcan estrictas, pueden ser manipuladas si exponen puntos de entrada en parámetros dinámicos. También subraya la importancia de mantener las directivas CSP completamente controladas desde el servidor y evitar cualquier forma de interpolación basada en parámetros del usuario.

Solucion
Aqui lo que podemos ver es que nos podemos aprovechar de lo errores estipulados dentro del csp 
![[Pasted image 20250718194157.png]]
aqui tratamos de poner un etiqeuta sencilla pero vemos que podemos tener adquisicion por medio del token
https://0a5600a1042dfc5ed8ddac0500580081.web-security-academy.net/?search=%3Cscript%3Ealert(0)%3C%2Fscript%3E&token=;script-src-elem%20%27unsafe-inline%27
