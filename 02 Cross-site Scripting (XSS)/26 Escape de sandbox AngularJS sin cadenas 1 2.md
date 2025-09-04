En esta clase de nivel ‘experto’, trabajamos con una vulnerabilidad de ‘XSS reflejado’ en una aplicación que utiliza AngularJS con restricciones avanzadas. La inyección ocurre dentro de una expresión Angular, pero el entorno está configurado para evitar el uso de ‘eval’ y bloquear por completo cualquier intento de utilizar cadenas de texto.

El enfoque consiste en usar funciones nativas de JavaScript para construir cadenas de forma indirecta. Aprovechamos el método ‘**toString()**‘ y la propiedad ‘**constructor**‘ para acceder al prototipo de los objetos y redefinir cómo se comportan. En concreto, se sobrescribe el método ‘**charAt**‘ del prototipo de las cadenas, lo que permite eludir el sistema de seguridad interno de AngularJS.

Luego pasamos una expresión al filtro ‘**orderBy**‘, y generamos el código deseado utilizando ‘**fromCharCode**‘ con los valores numéricos correspondientes a los caracteres de la cadena ‘**x=alert(1)**‘. Como hemos alterado el comportamiento interno de las cadenas, AngularJS permite que esta expresión se ejecute donde normalmente estaría bloqueada.

Este laboratorio demuestra cómo es posible romper entornos supuestamente seguros mediante manipulación de bajo nivel, sin depender de comillas o funciones evaluadoras explícitas.

Solucion
Para romper el sandbox de angular lo primero seria verificar en la pagina de cheet sheat y buscar lo de la version https://portswigger.net/web-security/cross-site-scripting/cheat-sheet
asi que lo primero seria verificar el codigo fuente o el script en la busquedad 

![Pasted image 20250717185117.png](imagenes/Pasted image 20250717185117.png)
