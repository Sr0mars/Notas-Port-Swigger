En esta primera parte del laboratorio nos centramos en descubrir si la aplicación es vulnerable a prototype pollution del lado cliente. Analizamos cómo es posible modificar el objeto global ‘**Object.prototype**‘ inyectando propiedades a través del query string, verificando la manipulación en la consola del navegador.

Este tipo de inyecciones nos permite alterar el comportamiento de objetos en toda la aplicación. Además, exploramos los archivos JavaScript para detectar posibles gadgets que podrían usarse como sinks, sentando así las bases para una explotación más avanzada en la segunda parte.

Este enfoque nos introduce a una técnica moderna y poderosa que afecta directamente al DOM desde el navegador.

Solucion
La web:
![Pasted image 20250831190234.png](imagenes/Pasted image 20250831190234.png)
la vulnerabilidad se puede presentar desde afuera por medio de un post o url
y en la url vamos a poner esto (?__proto__[foo]=bar)
![Pasted image 20250831190404.png](imagenes/Pasted image 20250831190404.png)
claramente no vamos a ver nada en la web pero si nosotro nos vamos a la consola y ponemos lo siguiente
![Pasted image 20250831190716.png](imagenes/Pasted image 20250831190716.png)
esto significa que hemos agregado incorporar una nueva propiedad a todos los objetos incluido los objetos vacios
esto lo interpreta asi algunos frameworks
![Pasted image 20250831191113.png](imagenes/Pasted image 20250831191113.png)


