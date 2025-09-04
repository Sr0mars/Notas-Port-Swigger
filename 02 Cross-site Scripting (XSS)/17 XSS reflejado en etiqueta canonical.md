En esta clase trabajamos con un XSS reflejado poco convencional, donde el punto vulnerable es una etiqueta utilizada para definir la URL canónica de la página. Aunque el sistema filtra los signos angulares para evitar aperturas de etiquetas nuevas, permite la inyección de atributos dentro de una etiqueta existente.

Aprovechamos este comportamiento para insertar atributos como accesskey y onclick, que nos permiten asociar una acción concreta —en este caso, la ejecución de código— a una combinación específica de teclas.

El exploit se construye de forma que, al presionar una combinación como Alt+Shift+X, el navegador dispare un evento que ejecuta la función deseada. Aunque no ocurre de forma automática al cargar la página, se considera válida ya que no requiere interacción directa con el contenido visible ni clics por parte del usuario.

Este laboratorio demuestra cómo atributos aparentemente inofensivos pueden ser utilizados como vectores de ejecución, y cómo el contexto de inyección —incluso en elementos como enlaces— puede tener implicaciones de seguridad si no se controla adecuadamente.

Solucion 
Esto solo funciona en en chrome asi que no lo abrimos ahi ya estando por alli lo que vamos a hacer es checar el codigo fuente y vemos en la url se abrio unas comillas asi que lo ideal es poner un signo de interrogacion y despues de eso otra comiila ?'
tal que no va mostrar esto
![Pasted image 20250714191931.png](imagenes/Pasted image 20250714191931.png)
entonces ahora podemos injectar palabras
![Pasted image 20250714192023.png](imagenes/Pasted image 20250714192023.png)
y con esto se puede poner un atajo que esto hace que hagamos que pase "algo"  ?'accesskey='x'onclick='alert(0)'
esto lo que hace que al momento de darle Ctrl+x o alt+ctrl+x o alt+x ya dependera del sistema operativo nos muestre el mensaje
![Pasted image 20250714192835.png](imagenes/Pasted image 20250714192835.png)




