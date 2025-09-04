En esta lección exploramos una inyección SQL ciega donde no hay retroalimentación visible ni diferencias temporales en la respuesta, ya que la consulta se ejecuta de forma asíncrona. Sin embargo, es posible generar interacciones fuera de banda (out-of-band) mediante técnicas de exfiltración pasiva.

La vulnerabilidad reside en la cookie ‘**TrackingId**‘, que es inyectada en una consulta SQL. Aprovechamos esta situación para insertar un payload que provoca una resolución DNS hacia un dominio controlado, utilizando la funcionalidad de Burp Collaborator.

Combinamos la inyección SQL con una entidad externa en XML (**XXE**) que genera una solicitud automática a un subdominio de Collaborator, confirmando así que la inyección fue ejecutada aunque no haya evidencia directa en la respuesta HTTP.

Esta clase introduce un enfoque más avanzado de explotación cuando no hay errores, retardos ni cambios visibles, y prepara el terreno para el siguiente paso: la exfiltración real de datos usando canales fuera de banda.

