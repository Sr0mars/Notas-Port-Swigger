En esta clase analizamos una vulnerabilidad de inyección SQL ciega basada en tiempo. La aplicación no muestra errores ni cambios en la respuesta al procesar la cookie ‘**TrackingId**‘, pero ejecuta las consultas de forma síncrona.

Aprovechamos este comportamiento para inyectar una función de retardo (**pg_sleep**) y medir el tiempo de respuesta del servidor. Si la consulta tarda en responder, podemos deducir que se ha ejecutado correctamente.

Este tipo de técnica es fundamental cuando no tenemos mensajes de error ni resultados visibles, permitiéndonos extraer información de forma indirecta a través del comportamiento temporal de la aplicación.

Solucion

Lo primero identificar el tipo de bases de datos a la cual nos estamos enfrentando
![Pasted_image_20250704115850.png](Imagenes/Pasted_image_20250704115850.png)
En este caso resulto ser PostgreSQL '||pg_sleep(2)-- -
![Pasted_image_20250704120200.png](Imagenes/Pasted_image_20250704120200.png)
