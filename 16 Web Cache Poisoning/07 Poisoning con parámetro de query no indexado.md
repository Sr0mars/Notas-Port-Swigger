Este laboratorio trata sobre una vulnerabilidad de web cache poisoning provocada por un parámetro que no forma parte de la clave usada por la caché, a pesar de ser procesado y reflejado en la respuesta. Esto permite que un atacante genere una versión maliciosa de la página que se almacene en caché y se entregue luego a usuarios legítimos.

Se identifica un parámetro como ‘**utm_content**‘ usando herramientas como Param Miner. A pesar de que el resto de la query string sí influye en la caché, este parámetro concreto no lo hace, lo que permite inyectar un payload como parte de su valor y que este se refleje en la página cacheada. Una vez envenenada la caché, cualquier usuario que acceda a la home sin ese parámetro recibirá la versión modificada. El laboratorio se resuelve cuando el usuario víctima accede y se ejecuta el contenido inyectado.

Solucion
de igual manera interceptamos la pagina principal
![Pasted_image_20250821220002.png](Imagenes/Pasted_image_20250821220002.png)
entonces con el parametro utm aplicamos la injeccion
![Pasted_image_20250821220141.png](Imagenes/Pasted_image_20250821220141.png)
y recargamos la pagina
![Pasted_image_20250821220206.png](Imagenes/Pasted_image_20250821220206.png)

