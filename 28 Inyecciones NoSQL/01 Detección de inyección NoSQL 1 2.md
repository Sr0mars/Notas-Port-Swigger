En esta clase analizamos cómo un filtro de categoría basado en MongoDB es vulnerable a inyección NoSQL.

Observamos un error de sintaxis al introducir caracteres especiales, lo que nos lleva a probar cargas útiles válidas en JavaScript. Mediante condiciones booleanas como ‘ **&& 1 &&** ‘ y expresiones que siempre evalúan a verdadero, conseguimos modificar la lógica de la consulta y forzamos al sistema a mostrar productos no publicados, confirmando la inyección.

Solucion
![Pasted_image_20250902001142.png](Imagenes/Pasted_image_20250902001142.png)
La web:
![Pasted_image_20250902001358.png](Imagenes/Pasted_image_20250902001358.png)
si nosotros nos vamos alguna categoria y aplicamos una simple comilla en la url ' para ver que se acontece
![Pasted_image_20250902001547.png](Imagenes/Pasted_image_20250902001547.png)
nos sale este error
![Pasted_image_20250902001602.png](Imagenes/Pasted_image_20250902001602.png)


