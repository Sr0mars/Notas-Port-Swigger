En este laboratorio nos enfrentamos a una vulnerabilidad de tipo open redirection basada en el DOM. El comportamiento vulnerable se produce al hacer clic en un enlace que evalúa un parámetro url directamente desde el fragmento del location.href sin realizar ninguna validación.

El enlace ejecuta un pequeño script que extrae con una expresión regular el valor del parámetro url y redirige al usuario allí, lo cual puede ser aprovechado para enviar a la víctima a un dominio externo controlado por un atacante.

Para explotar el fallo, construimos una URL que apunta al sitio vulnerable incluyendo como valor del parámetro url la dirección del exploit server. Cuando la víctima accede, se realiza la redirección automática hacia el servidor del atacante.

Solucion
le damos una revision a la pagina y tambien al codigo fuente
![Pasted_image_20250727174045.png](/Imagenes/Pasted_image_20250727174045.png)
Codigo fuente
![Pasted_image_20250727174156.png](/Imagenes/Pasted_image_20250727174156.png)
En este caso no vemos nada el codigo esta limpio vamos a revisar en la pagina aver si encontramos algo
en la seccion de post hasta abajo en la seccion de comentarios
![Pasted_image_20250727174450.png](/Imagenes/Pasted_image_20250727174450.png)
encontramos esto
![Pasted_image_20250727174517.png](/Imagenes/Pasted_image_20250727174517.png)
Este código busca una URL en la barra de direcciones, y si encuentra algo como `?url=https://ejemplo.com`, redirige al usuario allí al hacer clic. Si no encuentra nada, va a la raíz (`/`). **Puede ser inseguro si no se valida esa URL**, y debe manejarse con cuidado para evitar redirecciones abiertas.
entonces es tan sencillo como poner (&url=) la pagina donde queremos que nos rediriga
![Pasted_image_20250727174903.png](/Imagenes/Pasted_image_20250727174903.png)
y listo
![Pasted_image_20250727175000.png](/Imagenes/Pasted_image_20250727175000.png)
