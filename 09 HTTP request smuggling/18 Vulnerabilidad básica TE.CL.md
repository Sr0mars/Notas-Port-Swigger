En esta clase realizamos un ataque HTTP request smuggling de tipo TE.CL, donde el front-end acepta chunked encoding, pero el back-end no lo soporta. Aprovechamos esta diferencia para inyectar una petición que será reinterpretada por el back-end como si usara el método GPOST. Este escenario nos permite verificar la vulnerabilidad cuando la respuesta del servidor indica que no reconoce ese método, demostrando un desincronizado exitoso.

Solucion
Vamos a interceptar cambiamos al metodo y el http1
![Pasted image 20250809233204.png](imagenes/Pasted image 20250809233204.png)
