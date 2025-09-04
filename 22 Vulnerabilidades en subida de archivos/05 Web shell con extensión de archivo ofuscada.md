En esta clase trabajamos con una funcionalidad de subida que bloquea archivos por extensión, permitiendo solo imágenes con .jpg o .png. Para evadir esta restricción, usamos una técnica clásica de ofuscación: añadir un null byte codificado en la URL (%00) seguido de una extensión permitida, como .jpg.

Debido a cómo ciertos lenguajes o configuraciones interpretan el null byte, el sistema almacena y trata el archivo únicamente con la extensión real, .php, ignorando lo que viene después. Así conseguimos subir y ejecutar una shell PHP, accediendo a información sensible del servidor. Esta técnica muestra cómo detalles aparentemente menores en el tratamiento de cadenas pueden derivar en vulnerabilidades críticas.

Solucion
nos logeamos tratamos de subir nuestra shell y nos sale esto
![[Pasted image 20250830205001.png]]
ahora nos vamos al historico
![[Pasted image 20250830205053.png]]
entonces lo que podemos hacer es poner un %00.php que basicamente se supone que ignora la extencion de tal manera que nos permite subir el archivo (esto se debe la version de php que es vieja)
![[Pasted image 20250830205551.png]]
y ya solo copiamos y pegamos
![[Pasted image 20250830205751.png]]
