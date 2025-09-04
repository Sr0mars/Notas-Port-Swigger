En esta clase seguimos trabajando con inyecciones SQL ciegas, pero esta vez el indicador de éxito o fallo no es el contenido de la respuesta, sino si se genera un error visible en la aplicación.

La vulnerabilidad se encuentra en una cookie de seguimiento (**TrackingId**). La aplicación no muestra directamente los resultados de la consulta, pero sí muestra una respuesta distinta si se provoca un error en la ejecución de la consulta SQL.

Aprovechamos esto para:

- Confirmar que la consulta es vulnerable a inyección.
- Verificar que existe una tabla ‘**users**‘ y un usuario ‘**administrator**‘.
- Descubrir la longitud de la contraseña del administrador.
- Extraer la contraseña carácter por carácter, forzando errores solo cuando la condición evaluada es verdadera.

Para provocar errores intencionados, se usa la función ‘**TO_CHAR(1/0)**‘ (división por cero en Oracle), dentro de expresiones **‘CASE WHEN**‘ que evalúan condiciones booleanas. La idea es generar un error solo cuando la condición se cumple, lo que permite inferir información sin necesidad de ver los resultados directamente.

**Quédate con esto**: Aunque la aplicación no devuelva datos visibles ni mensajes directos, es posible extraer información sensible provocando errores intencionados y observando cómo responde el sistema. Este tipo de ataque es potente y silencioso.
