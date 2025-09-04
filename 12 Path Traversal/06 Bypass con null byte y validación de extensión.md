La aplicación intenta asegurar que los archivos solicitados terminen en .png, pero no considera el uso del byte nulo (**%00**).

Este carácter indica el final de cadena para muchas funciones en lenguajes como C. Al enviar ‘**https://hack4u.io/../etc/passwd%00.png**‘, el servidor interpreta solo lo anterior al **%00**, accediendo así a ‘**/etc/passwd**‘ a pesar de que la validación de extensión aparentemente se cumple.

Solucion
lo mismo 
![Pasted image 20250814223857.png](imagenes/Pasted image 20250814223857.png)
