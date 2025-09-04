En esta clase abordamos un XSS basado en DOM donde el código vulnerable utiliza una función que genera contenido HTML directamente en la página, tomando los datos desde la parte de búsqueda de la URL, específicamente desde el parámetro que indica el identificador de una tienda.

El fragmento dinámico se inserta dentro de una lista desplegable, por lo que cualquier valor enviado mediante ese parámetro se convierte en una nueva opción dentro del menú. Este comportamiento no incluye ninguna validación o codificación, lo que nos permite modificar la estructura del HTML de forma intencionada.

Para explotar la vulnerabilidad, rompemos la estructura del menú y añadimos un elemento adicional con un comportamiento malicioso, que se ejecuta automáticamente cuando el navegador intenta procesarlo.

Este laboratorio refuerza el concepto de que, cuando se generan elementos HTML a partir de datos controlables por el usuario, incluso dentro de componentes comunes como listas desplegables, puede abrirse una puerta directa a la ejecución de código si no se filtran correctamente las entradas.

Solucion
El campo vulnerable se presenta en el apartado de check stock cuando desplegamos la caja ![[Pasted image 20250708172532.png]]
Revisando un poco el codigo no puede decir que en el campo document.write podemos ver que podemos insertar codigo mediante la url
por medio del storeID
&storeId=Ya estuvO
![[Pasted image 20250708173103.png]]
&storeId=Ya estuvO
![[Pasted image 20250708173442.png]]
Algo que se puede hacer es viendo el script seria cerrar la etiqueta option y la etiqueta Selected y poder poner un pequeño script
un prueba seria asi
![[Pasted image 20250708174046.png]]
&storeId=</option></select><h1>Hola</h1>
y aqui tenemos un potencial XSS
![[Pasted image 20250708174237.png]]
