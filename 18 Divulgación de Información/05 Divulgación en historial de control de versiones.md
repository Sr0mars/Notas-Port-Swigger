En esta clase exploramos cómo la exposición del directorio ‘**.git**‘ puede revelar información sensible. Al descargar el repositorio completo desde el servidor, accedemos al historial de commits y encontramos uno en el que se eliminó una contraseña hardcodeada del fichero ‘**admin.conf**‘.

Aunque en el código actual ya no está presente, el diff del commit aún contiene la contraseña en texto claro. Utilizamos esa información para iniciar sesión como administrador, acceder al panel de administración y eliminar al usuario carlos, completando así el laboratorio.

Solucion
entonces para encontrar la version aqui podemos emplear FB con gobuster
![Pasted image 20250827224641.png](imagenes/Pasted image 20250827224641.png)
tal que nos da un directorio .git
vemos esto en la url
![Pasted image 20250827224948.png](imagenes/Pasted image 20250827224948.png)
asi que vamos a descargarlo (wget -r https://YOUR-LAB-ID.web-security-academy.net/.git/)
![Pasted image 20250827225448.png](imagenes/Pasted image 20250827225448.png)
tal que podemos ver una vez descargado todo lo que contiene
![Pasted image 20250827225759.png](imagenes/Pasted image 20250827225759.png)
y mas abajo vemos que se modifico la contraseña por lo cual esa es la que vamos a copiar y pegar
![Pasted image 20250827225902.png](imagenes/Pasted image 20250827225902.png)
nos logeamos
![Pasted image 20250827225940.png](imagenes/Pasted image 20250827225940.png)
ahora lo siguiente es eliminar al usuario carlos
![Pasted image 20250827230011.png](imagenes/Pasted image 20250827230011.png)
