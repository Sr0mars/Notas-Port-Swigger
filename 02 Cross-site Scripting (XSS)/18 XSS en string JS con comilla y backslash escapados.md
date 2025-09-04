En esta clase abordamos un XSS reflejado que se produce dentro de una cadena de texto en un bloque de JavaScript. El valor de entrada del usuario es reflejado en una variable delimitada por comillas simples, y tanto estas comillas como las barras invertidas están escapadas para dificultar la inyección.

Al intentar romper la cadena directamente, observamos que los caracteres clave quedan neutralizados, impidiendo ejecutar código dentro del mismo contexto. La estrategia, entonces, consiste en cerrar la etiqueta de script actual e insertar una nueva, completamente separada, que contenga la instrucción maliciosa.

De este modo, el contenido inyectado no depende de romper la cadena desde dentro, sino de interrumpir el bloque de código y generar uno nuevo fuera del contexto protegido. El navegador interpreta esta estructura como válida, permitiendo la ejecución de la función deseada.

Este laboratorio enseña una técnica de evasión muy útil para entornos donde los caracteres de escape son aplicados, pero el análisis del contexto permite insertar etiquetas completas que se interpretan igualmente como ejecutables por el navegador.

Solucion
aqui empezamos con lo de siempre vamos a poner testing en el buscador y vemos que trae el  codigo podemos ver que existe una variable que esta almacenando la cadena testing podemos probar con espacarla injectandole codigo
![Pasted_image_20250714193626.png](/Imagenes/Pasted_image_20250714193626.png)
![Pasted_image_20250714193639.png](/Imagenes/Pasted_image_20250714193639.png)
pero vemos que no funciona con la camilla asi que podemos poner un slash invertida pero tampoco no funciona
![Pasted_image_20250714193810.png](/Imagenes/Pasted_image_20250714193810.png)
pero nosotros podemos forzarlo con un simple </script> lo que hace esto es que salta la consulta que se esta realizando
![Pasted_image_20250714194040.png](/Imagenes/Pasted_image_20250714194040.png)
asi que podemos probar con un solo hola
![Pasted_image_20250714194231.png](/Imagenes/Pasted_image_20250714194231.png)

asi que podemos probar esto
</script><script>alert(0)</script>
![Pasted_image_20250714194549.png](/Imagenes/Pasted_image_20250714194549.png)
