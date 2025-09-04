En esta clase continuamos explorando técnicas avanzadas de explotación XXE ciega, esta vez utilizando una DTD externa maliciosa para exfiltrar el contenido del archivo /etc/hostname. Como la aplicación no muestra la respuesta del servidor, debemos forzar que este realice una petición externa que contenga los datos deseados.

Preparamos un archivo DTD en nuestro exploit server que define una entidad para leer el archivo local y otra para enviar su contenido mediante una petición HTTP a Burp Collaborator. Luego referenciamos esta DTD desde la carga XML enviada al stock checker.

Al realizar la petición y observar actividad en Collaborator, incluyendo potencialmente el contenido del archivo, conseguimos demostrar y aprovechar la vulnerabilidad, incluso en un escenario completamente ciego. Esta técnica es especialmente útil cuando no hay ningún tipo de respuesta visible en la interfaz.


