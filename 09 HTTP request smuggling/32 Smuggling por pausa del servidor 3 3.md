En esta clase, construimos y lanzamos una petición completa contra la ruta ‘**/admin/delete**‘ incluyendo los parámetros ‘**username=carlos**‘ y el token CSRF correspondiente. Ajustamos el marcador de pausa para que solo afecte a la primera sección de encabezados y así evitar errores en la segunda solicitud.

Finalmente, tras 61 segundos de espera, confirmamos que la acción fue procesada correctamente y el laboratorio queda resuelto.

Solucion
Entonces viendo que ya funciono lo podriamos probar con el panel de admin/ y esto es lo que vemos
![Pasted_image_20250813202152.png](/Imagenes/Pasted_image_20250813202152.png)
entonces en este punto lo que podemos realizar es en el parametro smuggled en ves de redirigirilo al host lo redirigimos al localhost y realizamos el ataque de nuevo
![Pasted_image_20250813202350.png](/Imagenes/Pasted_image_20250813202350.png)
rebuscando en el codigo podemos ver un formulario
![Pasted_image_20250813202523.png](/Imagenes/Pasted_image_20250813202523.png)
codigo (<form style='margin-top: 1em' class='login-form' action='/admin/delete' method='POST'>
                        <input required type="hidden" name="csrf" value="k1lfCf2LEICJD5p15RKbU1gzEJExYqkk">
                        <label>Username</label>
                        <input required type='text' name='username'>
                        <button class='button' type='submit'>Delete user</button>
                    </form>)

📌 **En resumen:** Este formulario sirve para que un administrador ingrese el nombre de un usuario y lo elimine, enviando la petición al servidor con un token de seguridad.

⚠️ **Nota de seguridad**: Si este formulario está en una página accesible sin restricciones, podría permitir que cualquiera elimine usuarios. La ruta `/admin/delete` debe estar protegida con autenticación y validación.
![Pasted_image_20250813202834.png](/Imagenes/Pasted_image_20250813202834.png)
entonces ahora podemos modificar nuestro payload para que podamos elimianar al usuario
![Pasted_image_20250813203524.png](/Imagenes/Pasted_image_20250813203524.png)
y esperamos y en efecto se a realizado el ataque
![Pasted_image_20250813203503.png](/Imagenes/Pasted_image_20250813203503.png)
