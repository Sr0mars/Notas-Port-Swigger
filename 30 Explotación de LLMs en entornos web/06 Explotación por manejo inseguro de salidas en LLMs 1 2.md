En esta clase registramos un usuario nuevo y usamos el chat para probar si es vulnerable a XSS mediante una imagen malformada. Comprobamos que el LLM refleja contenido directamente en la interfaz, lo que permite ejecutar código JavaScript. Luego probamos una carga más peligrosa que, si no se detecta, podría eliminar cuentas.

También descubrimos que el LLM analiza parte del contenido malicioso, pero aún así es posible evadir su detección con ingeniería en el texto.

Solucion
Lo primero es registrarnos no comparten un email client activamos la cuenta y nos logemamos
una vez logeado probamos en e live chat si es vulnerable a XSS
![[Pasted image 20250902123624.png]]
vemos que nos sale la alerta
