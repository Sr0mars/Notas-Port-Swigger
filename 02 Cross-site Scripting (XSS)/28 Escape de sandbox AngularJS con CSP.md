En esta clase de nivel experto abordamos un entorno altamente restringido donde coexisten dos capas de protección: una política CSP que impide la ejecución directa de scripts no autorizados, y el sandbox de AngularJS, que filtra el acceso a objetos críticos como el contexto global del navegador.

Para evadir ambas restricciones, construimos un vector que utiliza una expresión Angular inyectada dentro de un evento enfocado. Aprovechamos el evento ng-focus para ejecutar código al activarse el elemento y accedemos al objeto del evento a través de una variable predefinida por Angular. Esta variable contiene una ruta hacia el objeto window, sin necesidad de referenciarlo directamente, lo que nos permite eludir la validación del sandbox.

La inyección se construye utilizando el filtro orderBy con un argumento malicioso. En lugar de invocar directamente la función de alerta, se asigna a una variable dentro del filtro, y esta se ejecuta cuando se alcanza el contexto de ejecución adecuado.

Esta lección demuestra cómo es posible encadenar múltiples técnicas para vulnerar aplicaciones modernas protegidas por frameworks y políticas de seguridad del navegador, haciendo uso de pequeñas brechas lógicas dentro de los mecanismos de aislamiento.

Solucion
De igual forma toca buscar en cheet sheet por CSP y utilizar el payload (https://portswigger.net/web-security/cross-site-scripting/cheat-sheet)
<input ng-focus=$event.composedPath()|orderBy:'(z=alert)(1)'>

![[Pasted image 20250718172329.png]]
![[Pasted image 20250718172623.png]]

y a nuestra victima lo mandaraiamos asi
<script>
location = 'https://0aa000e7038c1ef180980375002c00b1.web-security-academy.net/?search=<input id=x+ng-focus=$event.composedPath()|orderBy:%27(z=alert)(document.cookie)%27>#x';
</script>
