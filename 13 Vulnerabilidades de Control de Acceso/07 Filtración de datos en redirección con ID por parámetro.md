Modificamos el parámetro id en nuestra página de cuenta para apuntar a carlos.

Aunque el servidor nos redirige, en el cuerpo de la respuesta se filtra la API key de carlos, permitiendo obtener su información sin autorización.

Solucion
que pasa aqui que se redirige a otra ubicacion si nosotros tratamos de cambiar al usuario
![Pasted image 20250815182447.png](imagenes/Pasted image 20250815182447.png)
entonces esto lo vamos a interceptar
![Pasted image 20250815183328.png](imagenes/Pasted image 20250815183328.png)
entonces algo que se puede hacer con BS es ir a settings en proxy
![Pasted image 20250815183526.png](imagenes/Pasted image 20250815183526.png)
le damos en add y modificar
![Pasted image 20250815183636.png](imagenes/Pasted image 20250815183636.png)
esto lo que hace es cambiarnos el estado de error 302 al 200 OK
simplemente con eso al recargar de nuevo la pagina ya se mantendra estable
![Pasted image 20250815183813.png](imagenes/Pasted image 20250815183813.png)
(Recordar eliminar la  opcion de BS)
