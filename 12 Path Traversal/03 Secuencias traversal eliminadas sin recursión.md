La aplicación intenta mitigar el path traversal eliminando las secuencias ‘**../**‘, pero lo hace de forma no recursiva. Esto permite evadir el filtro usando variantes como ‘**….//**‘, que tras la normalización del sistema de archivos siguen interpretándose como una subida de directorio.

Usando ‘**….//….//etc/passwd**‘, logramos acceder a archivos sensibles como ‘**/etc/passwd**‘, demostrando la debilidad de este enfoque de filtrado.

Solucion
seguimos con lo mismo interceptamos la imagen en el BS
![Pasted_image_20250814222024.png](Imagenes/Pasted_image_20250814222024.png)
