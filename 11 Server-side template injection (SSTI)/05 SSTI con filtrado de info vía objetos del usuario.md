En esta clase descubrimos que el motor de plantillas vulnerable es Django. Aprovechamos el tag ‘**{% debug %}**‘ para listar objetos internos accesibles desde la plantilla, entre ellos el objeto **settings**. Luego, accedemos directamente a ‘**{{settings.SECRET_KEY}}**‘ para revelar la clave secreta del framework y resolver el laboratorio.

Esta clase demuestra cómo una inyección de plantillas puede convertirse en una filtración crítica de información.

Solucion
en este caso el error se ejectua dejando el campo sin nada
![Pasted image 20250814202313.png](imagenes/Pasted image 20250814202313.png)
![Pasted image 20250814202332.png](imagenes/Pasted image 20250814202332.png)
![Pasted image 20250814202615.png](imagenes/Pasted image 20250814202615.png)
pero investigando un poco nos encontramos con este payload que devuelve la secret key 
![Pasted image 20250814203231.png](imagenes/Pasted image 20250814203231.png)
