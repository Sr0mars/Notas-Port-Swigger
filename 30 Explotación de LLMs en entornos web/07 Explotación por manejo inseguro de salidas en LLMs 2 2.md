Después de validar el comportamiento del modelo, creamos una reseña disfrazando la carga XSS dentro de una frase natural. Esta reseña logra ejecutarse cuando el LLM responde a una consulta sobre el producto y refleja su contenido sin filtrar. Aplicamos esta técnica al producto que carlos suele consultar y dejamos el payload embebido en una reseña.

Cuando carlos pregunta al LLM, se ejecuta el XSS que elimina su cuenta, resolviendo el laboratorio.

Solucion
y algo que podemos poner en la seccion de comentarios de algun post es esto
![[Pasted image 20250902124615.png]]
nos regresamos al live chat y le preguntamos
![[Pasted image 20250902124747.png]]
y nos da como respuesta esto
![[Pasted image 20250902124819.png]]
asi que ahora nos vamos al post de la chaqueta
y ponemos el mismo comentario
Este producto me encanta. He podido personalizar este producto metiendo "<iframe src =my-account onload = this.contentDocument.forms[1].submit() >" impreso en la propia chaqueta

y ya solo esperamos y el laboratorio se resuelve esto por que el usuario carlos esta charlando con el LLM sobre este producto
![[Pasted image 20250902125255.png]]

y con esto resolvemos el laboratorio
