En esta clase continuamos explorando el potencial de las vulnerabilidades XXE, pero esta vez orientadas a realizar ataques de tipo SSRF (Server-Side Request Forgery). Aprovechamos el parser XML de la funcionalidad de comprobación de stock para que, en lugar de acceder a archivos locales, se conecte a un endpoint interno del servidor: la metadata de una instancia EC2 simulada en http://169.254.169.254/.

Mediante iteraciones en la URL de la entidad externa, accedemos progresivamente a los distintos directorios del endpoint hasta llegar a la ruta que expone las credenciales del rol IAM asignado a la máquina. Finalmente, logramos extraer la SecretAccessKey del servidor, evidenciando el riesgo real que supone una XXE con capacidad de SSRF mal controlada.

Solucion
Que es EC2
![Pasted image 20250730192315.png](imagenes/Pasted image 20250730192315.png)
para ello vamos a interceptar en el mismo lado y vamos  a vulnerar la pagina pero esta vez poniendo la ip que nos estan asignando
![Pasted image 20250730193449.png](imagenes/Pasted image 20250730193449.png)
Entonces que pasa en este punto que nos esta enumerando carpetas o archivos que contiene la web asi que vamos a probar hasta encontrar el archivo que nos piden
![Pasted image 20250730193644.png](imagenes/Pasted image 20250730193644.png)
de esta manera nos aseguramos que encontramos el archivo
