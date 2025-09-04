Partiendo del campo de token exfiltrado previamente, realizamos una inyección para extraer su valor carácter a carácter. Utilizando el patrón ‘**this.<campo>.match()**‘ y el método **$where**, logramos reconstruir el token de reseteo completo. Después, enviamos una solicitud manipulada con ese token y redefinimos la contraseña de carlos, accediendo finalmente a su cuenta.

Esta técnica demuestra cómo una mala validación en NoSQL puede comprometer usuarios de alto privilegio.

Solucion

esto lo mandamos al intruder {"username":"carlos","password":{"$ne":"test"},"$where":"Object.keys(this)[0].match('^.'{0}a.*')"}

![Pasted image 20250902015221.png](imagenes/Pasted image 20250902015221.png)



