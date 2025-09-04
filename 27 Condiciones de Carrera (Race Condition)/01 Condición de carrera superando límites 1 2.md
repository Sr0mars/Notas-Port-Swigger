En esta clase usamos Burp Suite Professional para detectar y aprovechar una condición de carrera durante el proceso de compra. Observamos que al aplicar un código de descuento, el servidor responde correctamente una única vez y bloquea los intentos posteriores.

Sin embargo, al usar la opción personalizada ‘**Trigger race condition**‘ de Burp, enviamos múltiples solicitudes en paralelo, logrando aplicar el descuento varias veces antes de que el backend actualice el estado de la sesión. Esto nos permite reducir el precio de un artículo costoso por debajo del crédito disponible y completar la compra exitosamente.

Esta clase demuestra cómo el tiempo y la concurrencia pueden ser vectores de explotación efectivos en operaciones aparentemente seguras.

Solucion
![[Pasted image 20250901180621.png]]
La web:
![[Pasted image 20250901180712.png]]
nos logeamos
![[Pasted image 20250901180810.png]]
