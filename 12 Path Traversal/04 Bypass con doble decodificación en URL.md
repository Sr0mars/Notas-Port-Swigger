En este caso, la aplicación bloquea directamente las secuencias ‘**../**‘, pero comete el error de decodificar la entrada una vez más después del filtrado. Aprovechamos esto utilizando ‘**..%252f**‘, que al ser decodificado dos veces se transforma en ‘**../**‘, permitiéndonos realizar un path traversal efectivo.

Con esta técnica, logramos acceder al archivo ‘**/etc/passwd**‘, evidenciando cómo una decodificación extra puede introducir vulnerabilidades graves.

Solucion

lo mismo de los otros laboratorios interceptamos la imagen
![Pasted_image_20250814222805.png](/Imagenes/Pasted_image_20250814222805.png)
