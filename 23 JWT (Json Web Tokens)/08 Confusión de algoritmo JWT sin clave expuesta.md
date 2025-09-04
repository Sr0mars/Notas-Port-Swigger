En esta clase nos enfrentamos a una confusión de algoritmos en JWT sin que el servidor exponga públicamente su clave. A pesar de ello, logramos deducir la clave pública RSA que utiliza para validar los tokens, a partir de dos JWT generados legítimamente tras iniciar sesión.

Usamos la herramienta **sig2n**, que permite reconstruir valores matemáticamente posibles de la clave pública analizando las firmas. Tras identificar la clave válida, la usamos como si fuera una clave secreta con el algoritmo HS256, firmando un token falso que nos identifica como administrador.

Solucion
entonces la idea es interceptar 2 JWT y ejecutar docker
nos copiamos el primero
![Pasted image 20250831015731.png](imagenes/Pasted image 20250831015731.png)
dejamos de interceptar nos deslogeamos y nos volvemos a logear
![Pasted image 20250831015834.png](imagenes/Pasted image 20250831015834.png)
y volvemos a interceptar
copiamos nuevamente la JWT y pegamos
![Pasted image 20250831015957.png](imagenes/Pasted image 20250831015957.png)
esperamos a que termine
![Pasted image 20250831020314.png](imagenes/Pasted image 20250831020314.png)
y aqui la cuestion seria mandamos esto al repeater
![Pasted image 20250831020405.png](imagenes/Pasted image 20250831020405.png)
la idea sustituir cada uno de estos en la cookie del repeater hasta que me de codigo de estado 200
![Pasted image 20250831020506.png](imagenes/Pasted image 20250831020506.png)
y el penultimo me dio estado 200
![Pasted image 20250831020759.png](imagenes/Pasted image 20250831020759.png)
y este valor lo podemos usar
![Pasted image 20250831020833.png](imagenes/Pasted image 20250831020833.png)
nos copiamos esto
![Pasted image 20250831020953.png](imagenes/Pasted image 20250831020953.png)
generamos una una key symetrica
![Pasted image 20250831021024.png](imagenes/Pasted image 20250831021024.png)
nos regresamos al intercep y modificamos el wiener por administrator tambien el alg lo cambiamos ya solo le damos al sign
![Pasted image 20250831021125.png](imagenes/Pasted image 20250831021125.png)
copiamos la cookie y la pegamos en la web eliminamos al usuario carlos y fin
![Pasted image 20250831021237.png](imagenes/Pasted image 20250831021237.png)


