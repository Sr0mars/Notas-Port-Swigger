Mientras que en la clase anterior se clobberizaba la propiedad ‘**attributes’** para desactivar el filtrado de atributos peligrosos, en esta continuación se estudian otros objetivos dentro del DOM que pueden ser manipulados de forma similar, como ‘**name’**, ‘**id’**, o incluso propiedades internas de objetos que ciertos frameworks de saneamiento no esperan que puedan ser sobreescritas.

Se introduce además una nueva técnica para lograr la ejecución del payload sin interacción del usuario, aprovechando fragmentos en la URL combinados con el foco automático de ciertos elementos del DOM. El atacante prepara una estructura HTML aparentemente inofensiva, pero que al ser renderizada en el navegador y manipulada mediante un ‘**iframe’**, activa eventos como ‘**onfocus’**, ‘**onmouseover’** o ‘**onerror’** desde atributos previamente no autorizados por el filtro.

La clase remarca cómo estos ataques funcionan especialmente bien en entornos donde hay librerías antiguas de filtrado o soluciones mal implementadas que no contemplan colisiones de identificadores ni la mutabilidad de objetos globales como ‘**window’**.

En resumen, se enseña cómo un atacante puede inyectar HTML válido, manipular propiedades internas del DOM mediante colisiones de identificadores y forzar eventos que desencadenen ejecución de código, todo ello sin necesidad de bypasses tradicionales como etiquetas rotas o JavaScript codificado, lo que convierte esta técnica en una de las más limpias y difíciles de detectar en entornos reales.

Solucion
![Pasted image 20250727215807.png](imagenes/Pasted image 20250727215807.png)
explicacion de los payloads
![Pasted image 20250727220417.png](imagenes/Pasted image 20250727220417.png)
1.- <iframe src=https://0a7100f003063792804403d9004800eb.web-security-academy.net/post?postId=9 onload="setTimeout(()=>this.src=this.src+'#x',500)">
2.- <form id=x tabindex=0 onfocus=print()><input id=attributes>
