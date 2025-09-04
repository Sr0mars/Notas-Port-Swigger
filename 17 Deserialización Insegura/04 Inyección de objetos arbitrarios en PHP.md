En este laboratorio, se analiza una vulnerabilidad crítica: la inyección de objetos arbitrarios en PHP. Tras acceder al código fuente, se descubre una clase con un método mágico ‘**__destruct()**‘ que borra el archivo definido en el atributo ‘**lock_file_path**‘.

Aprovechando esta funcionalidad, se construye manualmente un objeto serializado que apunta al archivo ‘**/home/carlos/morale.txt**‘. Al inyectarlo como cookie de sesión y ejecutar una petición, el objeto se deserializa y el método destructivo se dispara automáticamente.

Este ejercicio ilustra perfectamente cómo un atacante puede ejecutar acciones peligrosas al forzar la deserialización de objetos que no debería poder controlar.

Solucion
interceptamos despues de logearnos
![Pasted image 20250826212118.png](imagenes/Pasted image 20250826212118.png)
y en este caso el codigo fuente del login nos da una ruta donde se encuentra un archivo php
![Pasted image 20250826212324.png](imagenes/Pasted image 20250826212324.png)
sin embargo al momento de poner esa direccion no encontramos nada
![Pasted image 20250826212703.png](imagenes/Pasted image 20250826212703.png)
sin embargo hay veces que se alamacena copias bin con tan solo poner (~)
![Pasted image 20250826212835.png](imagenes/Pasted image 20250826212835.png)

que hace este codigo?
Gestiona un archivo de plantilla con un sistema de bloqueo para evitar que se sobrescriba mientras está en uso.
¿Qué hace?
• 	Lee el contenido del archivo.
• 	Guarda nuevo contenido solo si no está bloqueado.
• 	Crea un archivo  como señal de que el archivo está siendo editado.
• 	Elimina el  automáticamente cuando el objeto se destruye (al final del script).
Es una forma básica de proteger archivos de edición simultánea

Por lo cual nosotros nos vamos a aprobechar de este codigo para poder eliminar el archivo para ello vamos a crear un objeto
(O:14:"CustomTemplate":1:{s:14:"lock_file_path";s:23:"/home/carlos/morale.txt";})

🔍 ¿Qué significa cada parte?
• 	 → Es un objeto () de la clase , cuyo nombre tiene 14 caracteres.
• 	 → El objeto tiene 1 propiedad.
• 	 →
• 	 → Es una propiedad llamada  (14 caracteres).
• 	 → Su valor es la cadena  (23 caracteres).
🧠 ¿Para qué sirve?
Este tipo de cadena se usa cuando quieres guardar el estado de un objeto para restaurarlo más tarde. Por ejemplo:
• 	Guardar en una sesión ()
• 	Escribir en un archivo
• 	Transmitir por red
En este caso, el objeto  tiene su propiedad  configurada con la ruta .

por lo cual ahora vamos a modificar la coockie pegando este nuevo objeto que acabamos de hacer
![Pasted image 20250826213826.png](imagenes/Pasted image 20250826213826.png)
aplicamos cambios y copiamos la cookie y la pegamos en la pagina
y recargamos
![Pasted image 20250826214052.png](imagenes/Pasted image 20250826214052.png)