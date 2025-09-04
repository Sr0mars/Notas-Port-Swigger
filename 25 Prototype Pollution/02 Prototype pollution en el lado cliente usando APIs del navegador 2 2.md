En esta segunda parte del laboratorio aprovechamos la contaminación del prototipo para abusar de un gadget ubicado en ‘**searchLoggerConfigurable.js**‘, donde **Object.defineProperty()** intenta proteger la propiedad ‘**transport_url**‘ pero omite definir su valor. Insertamos una propiedad value controlada en **Object.prototype**, lo que permite que se cree dinámicamente una etiqueta script con una URL personalizada.

Finalmente, usamos una URL ‘**data:’** como payload para ejecutar ‘**alert(1)**‘, demostrando la ejecución de código arbitrario. Esta clase muestra cómo una mala implementación de protección puede ser fácilmente eludida cuando se combinan técnicas como prototype pollution y DOM-based XSS.

Solucion
y bueno buscando en la web encontramos 2 archivos uno de ellos contiene informacion![Pasted image 20250831191500.png](imagenes/Pasted image 20250831191500.png)
que contiene este codigo
 ¿Qué hace ?
Esta función intenta enviar datos a un servidor usando .
• 	: dirección a la que se enviarán los datos.
• 	: objeto con los datos que se quieren enviar.
• 	: realiza una petición HTTP  al servidor.
• 	: permite que la petición continúe incluso si la página se está cerrando.
• 	: convierte el objeto en texto JSON para enviarlo.
• 	: si algo falla, muestra un error en consola.
🔧 Propósito: registrar o almacenar una consulta (query) en el servidor.

Este código sirve para registrar búsquedas realizadas en la URL de una página web. Si el usuario busca algo (por ejemplo, ?search=libros), esa información se envía al servidor para ser almacenada o analizada. También tiene la capacidad de cargar un script externo si se proporciona una URL de transporte.

por lo cual nosotros nos podemos aprovechar de value para poder verificar si se hace una consulta a bar de esta forma
![Pasted image 20250831192556.png](imagenes/Pasted image 20250831192556.png)
y esto lo podemos ver en el inspector
![Pasted image 20250831192656.png](imagenes/Pasted image 20250831192656.png)
entonces para injectar con un XSS podemos jugar con data un ejemplo seria una imagen
![Pasted image 20250831192746.png](imagenes/Pasted image 20250831192746.png)
entonces en la url podemos poner esto
data:,alert(1)
tal que me lo va interpretar ![Pasted image 20250831193016.png](imagenes/Pasted image 20250831193016.png)
y con esto hemos resuelto el lab
![Pasted image 20250831193105.png](imagenes/Pasted image 20250831193105.png)
