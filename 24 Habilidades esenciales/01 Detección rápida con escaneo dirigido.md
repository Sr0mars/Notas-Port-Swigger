En esta clase enfrentamos un reto contra reloj: descubrir una vulnerabilidad de lectura arbitraria de archivos en menos de 10 minutos. En lugar de escanear todo el sitio, lo cual consumiría demasiado tiempo, aplicamos una estrategia más inteligente y eficiente: identificar endpoints sospechosos e iniciar escaneos específicos sobre ellos con Burp Scanner.

Esto nos permite detectar patrones de comportamiento anómalo o posibles vectores de ataque más rápidamente. Una vez localizado el punto vulnerable, utilizamos nuestro conocimiento para explotarlo manualmente y obtener el contenido del archivo ‘**/etc/passwd**‘.

Esta clase refuerza el valor de la intuición combinada con herramientas automatizadas para optimizar tiempos durante una auditoría de seguridad.

Solucion
