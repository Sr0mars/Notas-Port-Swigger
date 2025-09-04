En esta clase trabajamos con una variante de client-side prototype pollution en la que el vector tradicional ‘**proto[propiedad]=valor**‘ no funciona, pero conseguimos el mismo efecto usando la sintaxis alternativa ‘**proto.propiedad=valor**‘.

Al modificar directamente ‘**Object.prototype**‘ de esta forma, inyectamos propiedades que serán heredadas por objetos posteriores. Analizando el código en ‘**searchLoggerAlternative.js**‘ encontramos un sink en la función **eval**, que utiliza el valor de ‘**manager.sequence**‘. Esta propiedad no existe por defecto, por lo que podemos controlarla a través de la contaminación del prototipo. Inicialmente el payload no se ejecuta debido a un carácter adicional que rompe la sintaxis, pero al añadir un guion al final del valor solucionamos el error y logramos ejecutar ‘**alert(1)**‘, resolviendo el laboratorio.

Esta clase muestra cómo pequeñas variaciones en los vectores de ataque pueden ser clave para explotar con éxito una vulnerabilidad.

Solucion
entonces lo primero seria verificar si es vulnerable
![[Pasted image 20250831194509.png]]
en esta ocacion nos sale undefined
verificamos si tiene algun objeto bar pero vemos que no
![[Pasted image 20250831194634.png]]
ahora nosotros lo podemos hacer de otra forma quitando los corchetes y poniendo un .
y vemos que este si no lo interpreta
![[Pasted image 20250831194807.png]]
lo corroboramos
![[Pasted image 20250831195112.png]]
nos vamos a depurador y vemos otra ves ese archivo lo copiamos y vamos a ver de que se trata
![[Pasted image 20250831195216.png]]
y vemos un eval y vemos que sequence no esta declarado asi que lo que podemos hacer es modificar la consulta
?__proto__.sequence=alert(1)
y ponemos un break point para ver que se tramita
![[Pasted image 20250831195817.png]]
podemos ver que se esta aplicando otro 1 despues del alert
asi que ponemos ponerlo un - para que lo elimine
![[Pasted image 20250831195952.png]]



