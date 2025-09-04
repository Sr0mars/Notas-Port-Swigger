En esta clase continuamos con la explotación de SSRF, centrándonos en cómo evadir defensas basadas en listas negras. La aplicación impide directamente ciertas direcciones como 127.0.0.1 y rutas sensibles como /admin, pero estas restricciones son débiles.

Utilizamos técnicas de evasión como redirecciones a direcciones IP alternativas (por ejemplo, 127.1) y codificación doble de caracteres (%2561 en lugar de a) para engañar al filtro. Gracias a esto conseguimos acceder al panel de administración interno y eliminar al usuario carlos, demostrando que los controles basados únicamente en listas negras no son una protección fiable contra SSRF.

Solucion
vamos a interceptar check stock u hacemos el urlcode y ctrl+u para el &
si nosotros vamos al grano veremos que no se acontece la solucion por lo cual no tenemos ninguna referencia al localhost
![[Pasted image 20250804194937.png]]
una solucion seria que nosotros podemos probar con hexadecimal
![[Pasted image 20250804195341.png]]
otra opcion es a decimal
![[Pasted image 20250804195542.png]]
![[Pasted image 20250804195734.png]]
pero de igual manera no podemos entrar pero y si quitamos admin nos sale invalid host
![[Pasted image 20250804195836.png]]
asi que es posible que el problema sea el admin por lo que podemos hacer es pasar 2 veces el urlcode allcaracters a la a
(1.- lo primero seria la a
2.- lo segun seria el porcentaje que deja la a)
![[Pasted image 20250804200226.png]]

pero en este caso no lo vamos a dejar en decimal si no que en el normal del localhost
![[Pasted image 20250804200746.png]]
y ya solo seria buscar el usuario copiar y eliminarlo
![[Pasted image 20250804200923.png]]
