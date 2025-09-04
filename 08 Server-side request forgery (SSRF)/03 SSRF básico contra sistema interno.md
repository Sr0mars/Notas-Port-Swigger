En esta clase exploramos un caso práctico de SSRF donde el servidor vulnerable interactúa con otro sistema interno que expone una interfaz de administración en la red privada. Aprovechamos la funcionalidad de verificación de stock para lanzar un escaneo controlado dentro del rango 192.168.0.X, variando la última parte de la IP.

Una vez identificamos qué IP responde en el puerto 8080 con una interfaz de administración accesible, manipulamos el parámetro vulnerable para interactuar con ella y ejecutar una petición que elimina al usuario carlos. Esta técnica demuestra cómo una SSRF aparentemente inocente puede convertirse en un vector para moverse lateralmente dentro de la infraestructura y comprometer otros servicios.

Solucion
De igual manera vamos a interceptar con BS el check stock (Recordad que nosotros devemos URLcodear el ampersan %26)
![Pasted image 20250804190829.png](imagenes/Pasted image 20250804190829.png)
En esta ocacion la pagina no se encuentra en el localhost por lo que esta mas segura pero de igual forma se puede enumerar para ver que encontramos
por lo cual sabemos que por el puerto 8080 exite una via potencial asi que vamos a pasarlo por el intruder
![Pasted image 20250804191402.png](imagenes/Pasted image 20250804191402.png)
asi que aqui lo vamos a sustituir es un rango numerico del 1 al 255 donde el numero 1 es donde se va hacer el ataque le tenemos que dar add
![Pasted image 20250804191639.png](imagenes/Pasted image 20250804191639.png)
y quitamos la casilla de urlcode y ya con esto configurado le damos start atacck
![Pasted image 20250804191805.png](imagenes/Pasted image 20250804191805.png)
una vez que acabe el ataque reagrupamos los codigos de estado y notamos que tenemos diferentes
el 400
![Pasted image 20250804193323.png](imagenes/Pasted image 20250804193323.png)
el 500
![Pasted image 20250804193410.png](imagenes/Pasted image 20250804193410.png)
pero el 404 es diferente lo cual es raro
![Pasted image 20250804193437.png](imagenes/Pasted image 20250804193437.png)

asi que podemos tratar de modificarlo
![Pasted image 20250804193646.png](imagenes/Pasted image 20250804193646.png)
y si miramos tenemos acceso al servidor que contempla asi que si miramos el codigo la ruta es la siguiente
![Pasted image 20250804193828.png](imagenes/Pasted image 20250804193828.png)
y con esto eliminamos al usuario carlos
![Pasted image 20250804193930.png](imagenes/Pasted image 20250804193930.png)

