En esta clase, continuamos trabajando una inyección SQL clásica aprovechando una vulnerabilidad en el parámetro de categoría que se usa para filtrar productos.

La aplicación hace una consulta SQL que busca productos de una categoría concreta y que ya estén publicados. El objetivo es alterar esa lógica para ver también los productos no publicados.

Para ello, interceptamos la petición que envía la categoría seleccionada y modificamos su valor añadiendo una condición ‘**OR 1=1**‘, lo que fuerza la consulta a devolver todos los productos, sin importar si están publicados o no. Además, se utiliza un comentario al final para ignorar el resto de la consulta original.

Este ataque demuestra cómo una simple manipulación en la entrada del usuario puede alterar completamente el comportamiento de la lógica SQL del backend.

**Quédate con esto**: Una inyección SQL bien colocada en una cláusula WHERE permite acceder a datos que deberían estar ocultos. Es una de las formas más básicas y efectivas de explotación.

![Pasted_image_20250701142912.png](Imagenes/Pasted_image_20250701142912.png)
Solucion
![Pasted_image_20250701143553.png](Imagenes/Pasted_image_20250701143553.png)
