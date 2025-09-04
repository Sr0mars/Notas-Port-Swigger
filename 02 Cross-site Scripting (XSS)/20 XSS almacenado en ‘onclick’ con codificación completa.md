En esta clase trabajamos con un XSS almacenado que afecta al campo de sitio web del sistema de comentarios. Este valor es posteriormente utilizado dentro de un manejador de eventos del tipo onclick asociado al nombre del autor del comentario.

El sistema aplica múltiples medidas de protección: codifica los signos angulares y las comillas dobles como entidades HTML, y además escapa tanto las comillas simples como las barras invertidas. Sin embargo, al observar cuidadosamente cómo se construye el atributo, descubrimos que aún podemos romper la estructura si inyectamos un valor cuidadosamente diseñado.

Utilizamos un valor de URL que contiene una secuencia manipulada para cerrar el contexto del atributo y ejecutar una función directamente. El carácter de escape que normalmente neutralizaría la comilla es absorbido por la estructura de la URL, permitiendo que el código se ejecute al hacer clic sobre el nombre del autor.

Este laboratorio enseña cómo incluso con múltiples capas de filtrado, pueden encontrarse formas de romper el contexto si se entiende cómo se evalúan los caracteres especiales en combinación con el navegador.

Solucion
igual que otras veces la vulnerabilidad esta en la seccion de comentarios es una vulnerabilidad onclick
podemos ver aqui el var tracker
![Pasted_image_20250714200530.png](/Imagenes/Pasted_image_20250714200530.png)

y podemos ver la comilla al final del callate asi que podemos intentar escaparla pero no funciona asi lo que podemos hacer es 
utilizar otro truquillo &apos que significa que es esto es una comilla
asi quedaria la sentencia
&apos;+alert(0)+&apos;
![Pasted_image_20250714203202.png](/Imagenes/Pasted_image_20250714203202.png)

eh aqui el resultado 
![Pasted_image_20250714203231.png](/Imagenes/Pasted_image_20250714203231.png)

