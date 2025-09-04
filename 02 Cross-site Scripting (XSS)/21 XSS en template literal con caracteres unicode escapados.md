En esta clase abordamos un XSS reflejado que ocurre dentro de una cadena de plantilla de JavaScript —también conocida como template literal—, donde el valor introducido por el usuario se refleja en tiempo de ejecución dentro de un fragmento delimitado por comillas invertidas.

El sistema aplica un filtrado agresivo que codifica signos angulares, comillas simples y dobles, barras invertidas y las propias comillas invertidas, bloqueando así inyecciones clásicas. Sin embargo, no restringe las expresiones contenidas entre el símbolo de dólar y llaves, que son interpretadas como código ejecutable dentro de la plantilla.

Aprovechamos esta brecha introduciendo una expresión que se evalúa directamente al cargar la página, sin necesidad de romper el delimitador original. Al estar el contenido ya dentro de una cadena ejecutable, el navegador interpreta la expresión de inmediato y ejecuta la función deseada.

Este laboratorio demuestra cómo las cadenas de plantilla pueden ser un punto crítico de inyección si no se filtran expresiones embebidas, y destaca la importancia de neutralizar todos los elementos interpretables dentro de estructuras modernas de JavaScript.

Solucion 
En esta ocacion tiene bastantes brechas de seguridad por lo cual a la hora de realizar un pequeño vistazo no escontramos con esto(`)
![Pasted image 20250717164835.png](imagenes/Pasted image 20250717164835.png)
pero en este caso cuando se utilizan este tipo de comillas [`]
se puede realizar lo siguiente
${alert(0)}