En esta clase trabajamos con una inyección SQL ciega, es decir, una situación donde la aplicación no muestra directamente los resultados de la consulta, ni devuelve errores, pero su comportamiento cambia dependiendo del resultado de una condición interna.

La vulnerabilidad está en la cookie de tracking que la aplicación utiliza para análisis. Aprovechamos ese valor para inyectar condiciones booleanas y observar si se cumple o no, basándonos únicamente en si aparece un mensaje del tipo “Welcome back” en la respuesta.

Usamos esta técnica para:

- Confirmar la existencia de una tabla ‘**users**‘ y un usuario ‘**administrator**‘.
- Determinar la longitud exacta de la contraseña del administrador.
- Extraer el valor carácter por carácter usando funciones como ‘**SUBSTRING**‘.

Este tipo de ataque requiere paciencia y precisión, ya que no vemos los datos directamente, pero con herramientas como Burp Repeater e Intruder, es posible automatizar gran parte del proceso.

**Quédate con esto**: Las inyecciones ciegas permiten obtener datos críticos incluso sin mensajes de error ni respuestas visibles, solo interpretando pequeños cambios en el comportamiento de la aplicación.
![Pasted image 20250702173215.png](imagenes/Pasted image 20250702173215.png)
