El recurso ‘**/js/localize.js**‘ es utilizado por el sitio web para manejar la traducción de textos. Al pasarle un parámetro ‘**lang**‘ manipulado, como ‘**lang=en?param=malicioso**‘, el archivo se ve afectado por contaminación de parámetros del lado cliente (client-side parameter pollution), ya que su valor no se codifica adecuadamente en la URL.

Esto permite interferir en cómo se comporta el script y preparar el entorno para la ejecución de un código arbitrario en el navegador de la víctima, en conjunto con otras vulnerabilidades.

Solucion
![Pasted image 20250822194802.png](imagenes/Pasted image 20250822194802.png)
entonces si nosotro modificamos el localize para ver el origin modificando claramente el cors poniendo a 1 nosotro podemos ver el Access control
![Pasted image 20250822195037.png](imagenes/Pasted image 20250822195037.png)
pero esto no estamos controlando el document.cookie
asi que nosotro podemos modificar el origin para que me sea interpretado como una nueva cabecera y tratar de manipular el document.cookie y como lo ariamos en formato ascii
de esta manera (Origin: x%0d%0aContent-Length:%208%0d%0a%0d%0aalert(1)$$$$)
de tal manera que se vera asi
![Pasted image 20250822195624.png](imagenes/Pasted image 20250822195624.png)
### ¿Qué intenta hacer?

Este payload busca **romper la forma en que el servidor maneja las cabeceras** para inyectar contenido controlado en la respuesta.

- Si el servidor es vulnerable, se produce lo que se llama **HTTP Response Splitting**.
    
- Eso permite al atacante **inyectar código JavaScript en la respuesta**, abriendo la puerta a un **XSS**.
    
- En este caso concreto, el atacante quiere que el navegador ejecute `alert(1)`.


entonces en el login redirect y en el localize vamos a emplear esto
Pragma: x-get-cache-key
que hace ?
`Pragma: x-get-cache-key` no hace nada en navegadores normales, pero **en algunos servidores/proxies/CDNs personalizados podría manipular la clave de caché**. Es un posible vector para **cache poisoning** o para evadir validaciones.
esto solo en el login
y eliminar el / para que nos de respuesta y ademas le vamos agregar el utm content que este lo ignora la cache
 y emplementamos esto
 ![Pasted image 20250822201839.png](imagenes/Pasted image 20250822201839.png)
 y el localized se veria asi
 ![Pasted image 20250822202048.png](imagenes/Pasted image 20250822202048.png)
 