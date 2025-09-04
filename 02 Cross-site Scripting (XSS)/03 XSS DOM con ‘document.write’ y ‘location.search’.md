En esta lección nos adentramos en el XSS basado en DOM, donde la vulnerabilidad no reside en el servidor, sino en cómo el código JavaScript del navegador procesa los datos de la URL.

El laboratorio utiliza una función que escribe directamente en la página el valor obtenido desde la parte de búsqueda de la URL (lo que va después del símbolo de interrogación). Este dato no es validado ni codificado, y se inserta dinámicamente mediante una función que genera HTML de forma directa.

Inicialmente observamos que al hacer una búsqueda cualquiera, el valor se refleja dentro de un atributo de imagen. A partir de ahí, construimos un vector de ataque que rompe el atributo e introduce código que se ejecuta en el navegador de la víctima.

Este tipo de XSS es especialmente común en aplicaciones ricas en JavaScript y demuestra cómo la lógica del lado cliente puede ser tan peligrosa como una mala validación en el backend.

Solucion 
si nosotros ponemos la injeccion normal no va pasar nada
![Pasted image 20250704162247.png](imagenes/Pasted image 20250704162247.png)
en cambio si le damos inspeccionar podemos verificar que en el codigo fuente claramente podemos cerrar la comilla que falta para que me le interprete como comentario y lo demas sea la injeccion 
![Pasted image 20250704162542.png](imagenes/Pasted image 20250704162542.png)
![Pasted image 20250704162656.png](imagenes/Pasted image 20250704162656.png)
![Pasted image 20250704162717.png](imagenes/Pasted image 20250704162717.png)
Entonces ya emos descubierto la vulnerabilidad por lo que podemos aplicar hacer pruebas
"><script>alert(0);</script>
![Pasted image 20250704163111.png](imagenes/Pasted image 20250704163111.png)
