En esta clase abordamos una vulnerabilidad escondida dentro de una estructura de datos poco común: una cookie compuesta por múltiples valores separados por dos puntos. Utilizamos la función Scan selected insertion point de Burp Scanner para analizar de forma precisa una parte específica de esa cookie, lo que nos permite descubrir una vulnerabilidad de Cross-Site Scripting almacenado que no sería evidente manualmente.

Tras confirmar la XSS, la aprovechamos para robar las cookies del administrador mediante una carga maliciosa que contacta con Burp Collaborator. Finalmente, reutilizamos esa cookie robada para acceder al panel de administración y eliminar al usuario Carlos.

Este laboratorio demuestra la utilidad de aplicar escaneos quirúrgicos en campos personalizados y estructuras no convencionales.

Solucion
