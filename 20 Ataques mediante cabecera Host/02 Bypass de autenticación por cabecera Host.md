En esta clase analizamos una vulnerabilidad lógica donde el servidor confía ciegamente en el valor de la cabecera Host para determinar si una petición proviene de un usuario con privilegios locales. Esta suposición es peligrosa, ya que el cliente puede modificar libremente esta cabecera.

Durante el laboratorio, al intentar acceder al panel /admin, se recibe un mensaje indicando que solo es accesible desde localhost. Modificando la cabecera Host a localhost usando Burp Repeater, el servidor acepta la petición como si viniera de un entorno de confianza, permitiéndonos acceder al panel de administración sin necesidad de autenticación real.

Desde ahí, se puede ejecutar la acción de eliminar al usuario carlos, demostrando cómo una validación deficiente del Host puede derivar en una escalada de privilegios y control completo sobre funcionalidades críticas.

Solucion
La web:
![Pasted image 20250829201753.png](imagenes/Pasted image 20250829201753.png)
visializamos que otras rutas existen en esta pagina con la ayuda de robots.txt
![Pasted image 20250829201940.png](imagenes/Pasted image 20250829201940.png)
vemos que tenemos un panel de admin y que solo esta disponible para usuario locales
![Pasted image 20250829202000.png](imagenes/Pasted image 20250829202000.png)
vamos a interceptar esto y lo que vamos hacer es modificar la cabecera host por un local host
tal que quedaria asi
![Pasted image 20250829202226.png](imagenes/Pasted image 20250829202226.png)
y pues obviamente en la respuesta tenemos lo que seria el codigo fuente y podremos eliminar el usuario carlos
![Pasted image 20250829202314.png](imagenes/Pasted image 20250829202314.png)
![Pasted image 20250829202338.png](imagenes/Pasted image 20250829202338.png)
![Pasted image 20250829202351.png](imagenes/Pasted image 20250829202351.png)

