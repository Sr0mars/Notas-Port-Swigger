En esta clase nos adentramos en un XSS basado en DOM que aprovecha una característica específica de AngularJS, un popular framework de JavaScript. La vulnerabilidad reside en cómo el sistema procesa expresiones dentro de directivas marcadas con un atributo especial en el HTML.

La funcionalidad afectada es un buscador, cuyo valor introducido se refleja dentro de un nodo HTML que está bajo el control de AngularJS. A pesar de que los signos angulares y las comillas están codificados, Angular permite la ejecución de expresiones mediante doble llave, lo que nos abre una vía alternativa para ejecutar código.

Utilizamos una expresión construida con métodos internos del framework para forzar la ejecución de una función maliciosa, demostrando que la entrada del usuario se evalúa directamente dentro del motor de plantillas.

Este laboratorio destaca cómo los entornos con frameworks modernos pueden presentar vectores de ataque muy diferentes a los clásicos, y cómo conocer las particularidades de cada tecnología es clave para su explotación y protección.

Solucion
Gracias al wapalizer podemos ver que tecnologias utiliza ![[Pasted image 20250708174644.png]]
Por lo cual no podemos utilizar las etiquetas vulnerables por lo cual se recomienda este repo de Gity HUB
https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/XSS%20Injection/5%20-%20XSS%20in%20Angular.md
![[Pasted image 20250708175334.png]]
![[Pasted image 20250708175542.png]]
![[Pasted image 20250708175641.png]]
