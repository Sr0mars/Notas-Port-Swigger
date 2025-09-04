En esta clase identificamos una vulnerabilidad de Server-Side Template Injection (SSTI) en el motor de plantillas Tornado. Mediante una combinación de sintaxis de plantillas y código Python embebido, conseguimos ejecutar comandos arbitrarios desde el servidor.

Esto nos permite borrar un archivo sensible de forma remota, demostrando el riesgo de interpolar entradas del usuario sin sanitización en contextos de código.

Solucion
![[Pasted image 20250814191402.png]]
asi que para ello vamos a logearnos y despues vamos a interceptar el apartado de submit que se encuentra en la parte de my account
![[Pasted image 20250814191145.png]]
en este caso se esta empleando tornado como template y esto se sabe causando un error en la parte de la solicitud la cual se puede emplear por BS
![[Pasted image 20250814192017.png]]
se aplica aqui
![[Pasted image 20250814192912.png]]
entonces esto se vera reflejado en algun post en el cual nosotros hemos publicado alguna cosa
![[Pasted image 20250814193053.png]]
entonces nosotros si aplicmaos una consulta con tornado
![[Pasted image 20250814193440.png]]
la consulta la estamos sacando de aqui
![[Pasted image 20250814193507.png]]
y si nosotros le damos a send y checamos el post obtenemos el usuario
![[Pasted image 20250814193551.png]]
y ya solo miramos el archivo que queremos eliminar y aplicamos la consulta
![[Pasted image 20250814193811.png]]
