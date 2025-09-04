HTMLJanitor es una librería pensada para filtrar contenido HTML malicioso, limitando los atributos permitidos y bloqueando potenciales vectores XSS. Sin embargo, su lógica interna se basa en comprobar si ciertos atributos están definidos dentro de una colección, y esa colección se accede mediante la propiedad ‘**attributes’**. Lo crítico aquí es que esta propiedad puede ser clobberizada.

La clase muestra cómo introducir un elemento con un identificador específico (por ejemplo, un ‘**input’** con id ‘**attributes’**) para sobrescribir la propiedad esperada. Al hacerlo, el filtro deja de funcionar como se esperaba, ya que ‘**attributes.length’** deja de existir o retorna ‘**undefined’**, y se permite la inclusión de atributos normalmente bloqueados, como ‘**onfocus’**.

Una vez inyectado el HTML malicioso, se utiliza el exploit server para forzar la ejecución automática del payload. Se hace mediante un iframe que carga la URL del post objetivo, y medio segundo después, añade un fragmento (**#x**) al final, lo que provoca que el navegador intente enfocar el elemento con ese ID. Ese elemento es un formulario creado en el comentario que, al recibir el foco, dispara el evento ‘**onfocus’** con el ‘**print()’** como payload.

Este tipo de técnica es especialmente peligrosa porque no requiere JavaScript complejo ni abusar de etiquetas exóticas; simplemente se aprovecha de cómo el DOM interpreta ciertos identificadores y de cómo los frameworks de sanitización pueden ser engañados si no manejan correctamente estos casos límite.

Solucion
