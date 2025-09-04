En esta clase abordamos una inyección de comandos del sistema operativo en modalidad ciega, usando la función de feedback de la aplicación. Aunque el resultado del comando no se muestra en la respuesta, conseguimos demostrar su ejecución provocando una pausa intencionada.

Al inyectar ‘**||ping -c 10 127.0.0.1||**‘ en el parámetro ‘**email**‘, el servidor ejecuta el comando y genera un retardo de 10 segundos, lo que confirma la vulnerabilidad.

Solucion
En esta ocacion el campo vulnerable se encuentra en este formulario
![Pasted image 20250813230951.png](imagenes/Pasted image 20250813230951.png)
y el campo se encuentra despues de email
![Pasted image 20250813231502.png](imagenes/Pasted image 20250813231502.png)