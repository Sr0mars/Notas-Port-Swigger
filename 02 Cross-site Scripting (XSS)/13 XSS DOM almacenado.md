En esta clase trabajamos con un XSS almacenado basado en DOM, donde el comentario malicioso se guarda en el servidor, pero es procesado y convertido en código ejecutable directamente en el navegador de quien lo visualiza.

La funcionalidad vulnerable se encuentra en el sistema de comentarios del blog. Para prevenir ataques, el sitio aplica una función de reemplazo que intenta codificar los signos angulares, pero lo hace incorrectamente: solo reemplaza la primera aparición en lugar de todas.

Aprovechamos este fallo insertando un par adicional de signos al principio del comentario. Estos primeros caracteres serán codificados y neutralizados, pero los siguientes no serán tocados, permitiendo que el navegador interprete y ejecute el contenido malicioso cuando se carga la página.

Este laboratorio demuestra cómo una protección mal implementada puede dar una falsa sensación de seguridad, y cómo es posible evadirla con simples técnicas de desbordamiento o saturación de filtros.

Solucion

En la seccion de comentarios es donde esta la vulnerabilidad
<script>alert(0)</script>
![Pasted image 20250708205012.png](imagenes/Pasted image 20250708205012.png)
y podemos ver en este punto que no podemos ver el cierre
![Pasted image 20250710154110.png](imagenes/Pasted image 20250710154110.png)
podemos ver que en la seccion no cierra la equiqueta pasamos aver el por que y parece que entoncramos una sanitizacion
![Pasted image 20250710154334.png](imagenes/Pasted image 20250710154334.png)
pasamos a verla en curl y podemos ver una pequeña sanitizacion en esta parte 
![Pasted image 20250710154839.png](imagenes/Pasted image 20250710154839.png)
lo podemos ver en la consola convierte los menor que y mas en otra cadena
![Pasted image 20250710154910.png](imagenes/Pasted image 20250710154910.png)
y esto parece que solo funciona en la primera cadena de script pero si ponemos o cerramos nuevamente la etiqueta parece que la evade
![Pasted image 20250710155433.png](imagenes/Pasted image 20250710155433.png)
y en caso que no agarra la etiqueta script podemos usar el img <><image src=0 onerror=alert(0)>

![Pasted image 20250710155651.png](imagenes/Pasted image 20250710155651.png)

