En esta clase trabajamos con un entorno donde la inyección de código se limita a un conjunto restringido de etiquetas permitidas. Todos los eventos JavaScript y los atributos href están bloqueados, lo que impide usar vectores clásicos como enlaces con scripts o atributos on-click.

Para evadir estas restricciones, utilizamos una estructura SVG compuesta que simula un enlace visual. Insertamos una etiqueta de animación dentro de un elemento interactivo y manipulamos un atributo gráfico permitido para que, al ser activado, modifique el valor del enlace con un esquema que ejecuta código.

La animación se activa de forma implícita al interactuar con el contenido, y dado que se encuentra dentro de un SVG, el navegador interpreta la secuencia de forma válida aunque los filtros bloqueen atributos estándar. Además, se incluye la palabra Click como anzuelo visual para atraer al usuario simulado del laboratorio a realizar la acción.

Este laboratorio demuestra cómo el uso creativo de etiquetas permitidas dentro de entornos gráficos como SVG puede servir para evadir restricciones avanzadas y ejecutar código malicioso en el navegador de la víctima.

Solucion

en este caso vamos a crear una etiqueta nueva que me permita animar el href
<svg><a><animate attributeName=href values=javascript:alert(0) /><text x=30 y=30>Click me!</text></a>
![[Pasted image 20250718174753.png]]
