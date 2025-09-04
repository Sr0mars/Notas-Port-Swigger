En esta clase trabajamos con un entorno de XSS reflejado donde la mayoría de etiquetas HTML estándar están bloqueadas, pero algunas relacionadas con SVG aún están permitidas, incluyendo ciertos eventos compatibles con esa tecnología.

La vulnerabilidad está en el buscador, que refleja la entrada del usuario directamente en la respuesta. Aunque intentos típicos de inyección son bloqueados, realizamos un análisis sistemático usando Burp Intruder para descubrir qué etiquetas y atributos aún son aceptados por el sistema.

Tras probar múltiples combinaciones, identificamos que algunas etiquetas del entorno SVG, como svg y animatetransform, junto con eventos como onbegin, no son filtradas y permiten la ejecución de código al momento de cargarse la página.

Aprovechamos esto para construir un vector que, sin intervención del usuario, desencadena una función en el navegador al iniciarse la animación SVG, completando con éxito el laboratorio.

Este caso demuestra cómo incluso los entornos con filtros activos pueden ser vulnerables si se dejan rutas menos comunes abiertas, como el espacio SVG, y destaca la importancia de validar tanto etiquetas como atributos y eventos asociados.

Solucion
Empesamos hacer lo mismo lo cual seria agarramos y ponemos una etique comun en el buscador lo interceptamos con BS nos vamos al intruder utilizamos las etiquetas y quitamos la casilla
Entonces el primer paso es entontrar las etiquetas que nos deja
![[Pasted image 20250711154502.png]]
lo siguente es investigar que significa esa etiqueta en este caso ocupa que le pongamos otra etiqueta que es la svg
![[Pasted image 20250711154624.png]]
asi que ponemos la sintaxix en el repeter y despues lo mandamos de nuevo al intruder para ponfigurar el payload y este caso nusetro payload va ser la a (tenemos que poner el espacion por %20 ya que es una peticion por get)
![[Pasted image 20250714190626.png]]
lo siguente seria localizar el evento para poner las etiquetas
En este caso vamos a utilizar en onbegin que es al comenzar asi que ponemos toda la url de esta manera
<svg><animateTransform onbegin=alert(0)>
![[Pasted image 20250714191013.png]]


