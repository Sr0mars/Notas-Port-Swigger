En esta clase abordamos un ataque SSRF básico aprovechando una funcionalidad de consulta de stock que realiza peticiones internas. Aunque el panel de administración no es accesible directamente desde el navegador, al interceptar la petición que hace la funcionalidad de stock, modificamos el parámetro correspondiente para forzar una petición a ‘**localhost**‘.

Esto nos permite interactuar con la interfaz de administración interna, identificar la URL para eliminar al usuario carlos, y ejecutar dicha acción a través de la misma funcionalidad vulnerable. Con esto conseguimos resolver el laboratorio accediendo a recursos internos sin privilegios directos.

Solucion
![[Pasted image 20250804190640.png]]