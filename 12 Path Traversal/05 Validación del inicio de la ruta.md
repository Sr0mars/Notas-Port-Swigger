En este escenario, la aplicación intenta validar que las rutas comiencen con ‘**/var/www/images/**‘, pero no restringe adecuadamente lo que viene después. Aprovechamos esto enviando una ruta como ‘**/var/www/images/https://hack4u.io/../etc/passwd**‘, que tras la resolución final accede al archivo sensible fuera del directorio permitido.

Esta clase demuestra cómo una validación superficial del inicio del path puede ser fácilmente evadida con secuencias de retroceso (**../**).

Solucion
Interceptamos y aplicamos
![Pasted_image_20250814223411.png](/Imagenes/Pasted_image_20250814223411.png)
