En esta clase abordamos una vulnerabilidad que requiere el uso conjunto de varias cabeceras HTTP para llevar a cabo un ataque de Web Cache Poisoning. El servidor utiliza información de cabeceras como ‘**X-Forwarded-Scheme**‘ y ‘**X-Forwarded-Host**‘ para construir redirecciones, pero no incorpora dichas cabeceras en su clave de caché.

Manipulando estas cabeceras es posible hacer que el servidor genere una redirección hacia un dominio controlado por el atacante, apuntando a un script JavaScript alojado en un exploit server con un payload malicioso, como ‘**alert(document.cookie)**‘.

Una vez que la respuesta es cacheada y el indicador ‘**X-Cache: hit**‘ lo confirma, cualquier usuario que acceda a la página durante ese periodo recibirá la versión envenenada del recurso. Esto permite ejecutar código JavaScript en el navegador de la víctima sin interacción por su parte.

Este laboratorio muestra cómo cabeceras múltiples, mal gestionadas, pueden combinarse para explotar fallos lógicos en la configuración del servidor y comprometer la seguridad de los usuarios.

Solucion
de igual manera interceptamos en la pagina princiapal y mandamos al repeter
en este caso vamos a implementar esta cabecera (X-Forwarded-Scheme)
![Pasted image 20250821204405.png](imagenes/Pasted image 20250821204405.png)
y tambien esta cabecera (X-Forwarded-host)
![Pasted image 20250821204507.png](imagenes/Pasted image 20250821204507.png)
pero si nosotros nos fijamos en la historico vemos que exite un redirect
![Pasted image 20250821204814.png](imagenes/Pasted image 20250821204814.png)
el cual esto lo podemos usar para nuestro exploit server asi que esto lo mandamos al repeater
entonces este nuevo repeater lo configuramos
![Pasted image 20250821205904.png](imagenes/Pasted image 20250821205904.png)
configuramos nuestro exploit
![Pasted image 20250821205931.png](imagenes/Pasted image 20250821205931.png)
y ya solo le damos send y recargamos la pagina
![Pasted image 20250821210038.png](imagenes/Pasted image 20250821210038.png)
