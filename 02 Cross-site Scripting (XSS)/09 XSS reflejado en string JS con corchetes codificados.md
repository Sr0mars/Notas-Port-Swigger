En esta clase trabajamos con un XSS reflejado que ocurre dentro de una cadena de texto en un fragmento de código JavaScript. Aunque los signos de apertura y cierre de etiquetas están codificados, el contexto vulnerable no está en HTML, sino en el propio lenguaje JavaScript.

La funcionalidad afectada es el sistema de seguimiento de búsquedas. Al introducir una consulta, el valor se refleja en una variable JavaScript como parte de una cadena. Esto permite al atacante cerrar esa cadena con comillas o caracteres especiales, insertar código adicional, y continuar la ejecución sin generar errores de sintaxis.

Utilizamos este enfoque para romper la cadena original y ejecutar una función maliciosa, demostrando así que la inyección es posible a pesar del filtrado parcial.

Este laboratorio introduce uno de los contextos más comunes y peligrosos en los que puede explotarse XSS: dentro del propio código del cliente, donde las medidas tradicionales de filtrado HTML no son suficientes para evitar el ataque.

Solucion
de nuevo lo que estamos haciendo es identificar en el codigo fuente que vulnerabilidad tiene script
![Pasted_image_20250707161919.png](Imagenes/Pasted_image_20250707161919.png)testing'; alert(0); var testing='probando
![Pasted_image_20250707162440.png](Imagenes/Pasted_image_20250707162440.png)
otra forma el chiste es encontrar el error de la comilla y cerrarlo
![Pasted_image_20250707162607.png](Imagenes/Pasted_image_20250707162607.png)
