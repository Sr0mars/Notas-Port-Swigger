En esta clase llevamos el XSS almacenado un paso más allá, enfocándonos en capturar las credenciales de un usuario legítimo en lugar de solo su cookie de sesión. El entorno vulnerable es un sistema de comentarios donde el código inyectado queda persistente y se ejecuta cuando un visitante visualiza el contenido.

Aprovechamos esta oportunidad para insertar campos de entrada personalizados en el comentario, imitando elementos ya existentes en la página. Añadimos un evento que, cuando el usuario introduce su contraseña, intercepta el valor junto con su nombre de usuario y los envía automáticamente al servidor público de Burp Collaborator.

Una vez que recibimos esta información en el panel de Collaborator, podemos utilizar las credenciales capturadas para iniciar sesión como la víctima, accediendo así directamente a su cuenta.

Este laboratorio demuestra cómo el XSS puede emplearse para técnicas de credential harvesting, especialmente cuando se combinan con ingeniería social y campos camuflados. También refuerza la importancia de tratar todo contenido generado por usuarios como potencialmente malicioso.
