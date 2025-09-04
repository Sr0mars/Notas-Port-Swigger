Construimos en PHP un objeto **CustomTemplate** que contiene un **Blog** como plantilla, y en su atributo ‘**desc**‘ insertamos un payload Twig que aprovecha la función ‘**registerUndefinedFilterCallback()**‘ para ejecutar ‘**rm /home/carlos/morale.txt**‘.

Empaquetamos este objeto dentro de un archivo PHAR, y lo convertimos en un JPG válido para poder subirlo como avatar. Esto lo logramos creando un polyglot (PHAR-JPG) que funcione como imagen pero sea interpretado por PHP como un archivo PHAR cuando se accede con ‘**phar://**‘.

Solucion
ahora entendiendo un poco el codigo lo que podemos hacer es un payload con la ayuda de un repositorio de git(https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Server%20Side%20Template%20Injection/PHP.md#twig)
![Pasted image 20250827212738.png](imagenes/Pasted image 20250827212738.png)
