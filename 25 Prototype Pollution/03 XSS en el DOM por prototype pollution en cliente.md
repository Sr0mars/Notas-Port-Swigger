En esta clase exploramos una vulnerabilidad de client-side prototype pollution que nos permite ejecutar JavaScript arbitrario manipulando **Object.prototype** desde la URL.

Identificamos una fuente de contaminación mediante el parámetro ‘**__proto__**‘ y analizamos los archivos JavaScript cargados por la página. En el archivo ‘**searchLogger.js**‘, descubrimos un gadget donde, si existe la propiedad ‘**transport_url**‘ en el objeto **config**, se inserta dinámicamente una etiqueta script en el DOM con un **src** controlable.

Aprovechamos esto para inyectar un valor malicioso que ejecuta ‘**alert(1)**‘, demostrando cómo una simple manipulación del prototipo puede derivar en una vulnerabilidad de XSS crítica.

Solucion
no encontramos en la web lo primero seria verificar si es vulnerable
![[Pasted image 20250831193256.png]]
como lo hacemos de esta manera
![[Pasted image 20250831193429.png]]
ahora si nos vamos el los recursos y vemos el js que tiene ahi
![[Pasted image 20250831193533.png]]
pero no podemos aplicar esto por que en esta ocacion ya no estaba redefinida  trasport_url
![[Pasted image 20250831193750.png]]
pero lo que si podemos hacer es esto /?__proto__[transport_url]=data:,alert(1)
y esto lo probamos en la url
![[Pasted image 20250831194118.png]]de modo que de esta forma resovemos el lab
![[Pasted image 20250831194157.png]]
