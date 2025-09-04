En esta primera parte del laboratorio usamos DOM Invader para detectar fuentes de prototype pollution presentes en la propiedad ‘**hash**‘ de la URL, es decir, en la parte posterior al símbolo ‘**#**‘. Activamos la opción de análisis de contaminación del prototipo y recargamos la página para que DOM Invader escanee los vectores disponibles.

Gracias a su capacidad de inspección automatizada, detectamos que es posible modificar ‘Object.prototype’ inyectando propiedades a través del fragmento de la URL, lo que nos permite preparar el terreno para una explotación más profunda. Esta clase demuestra cómo fragmentos aparentemente inofensivos pueden ser vectores potentes de ataque en el navegador.

Solucion
y bueno la idea es que usemos el navegador del BS y activemos la extencion que nos viene
![Pasted image 20250831230857.png](imagenes/Pasted image 20250831230857.png)
activamos la extencion nos vamos a attack types
y activamos el prototype y volvemos a recargar la pagina
![Pasted image 20250831230945.png](imagenes/Pasted image 20250831230945.png)
y esto lo vemos en el apartado de inspeccionar y vemos una nueva pestaña de dom
![Pasted image 20250831231115.png](imagenes/Pasted image 20250831231115.png)
y podemos ver 2 opciones
![Pasted image 20250831231432.png](imagenes/Pasted image 20250831231432.png)
la primera de test donde se automatiza y se hace la consulta
![Pasted image 20250831231510.png](imagenes/Pasted image 20250831231510.png)
y la segunda donde va scaneando los gadgets
![Pasted image 20250831231548.png](imagenes/Pasted image 20250831231548.png)
cuando termina el scaneo podemos ver que nos sale la opcion de exploit 
![Pasted image 20250831231621.png](imagenes/Pasted image 20250831231621.png)si le damos podemos ver que se ejecuta la consulta
![Pasted image 20250831231701.png](imagenes/Pasted image 20250831231701.png)
de igual forma alado del exploit vemos una opcion que se llama stack trace si le picamos podemos ver de donde viene el hitcallback
lo muestra en consola
![Pasted image 20250831232052.png](imagenes/Pasted image 20250831232052.png)
se supone que se emplea aqui
![Pasted image 20250831232218.png](imagenes/Pasted image 20250831232218.png)
si filtramos podemos ver que se emplea una variable
![Pasted image 20250831232354.png](imagenes/Pasted image 20250831232354.png)
y lo vemos mas arriba
![Pasted image 20250831232432.png](imagenes/Pasted image 20250831232432.png)
