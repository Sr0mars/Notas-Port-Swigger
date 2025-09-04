En esta clase analizamos un XSS reflejado que ocurre dentro de una cadena de texto en JavaScript. El valor reflejado del buscador se inserta en una variable delimitada por comillas simples. En este caso, las comillas simples están escapadas correctamente, y tanto los signos angulares como las comillas dobles están codificados como entidades HTML.

Sin embargo, la clave está en que las barras invertidas no se escapan, lo que nos permite introducir una de forma manual y romper el contexto de la cadena desde fuera.

Aprovechamos esta debilidad insertando una barra invertida seguida de una comilla escapada que finaliza la cadena, y después inyectamos una instrucción directa, separándola del código original con un operador y comentarios para evitar errores de sintaxis.

Este laboratorio muestra cómo es posible evadir filtros mixtos —HTML y JavaScript— si se detecta un punto débil en alguno de los mecanismos de escape, como en este caso con las barras invertidas no gestionadas correctamente.

Solucion
Empezamos con lo mismo asi que lo que podemos hacer es saltar las comillas 
![Pasted_image_20250714195019.png](Imagenes/Pasted_image_20250714195019.png)
Vemos que tiene filtro de sanitizacion
asi que en este caso vamos a probar con la aritmetica osea una operacion sencilla escapando de las comillas
'test'\'+alert(0);//
![Pasted_image_20250714195802.png](Imagenes/Pasted_image_20250714195802.png)
Lo que muestra la ventana emergente

