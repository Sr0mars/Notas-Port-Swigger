En esta segunda parte continuamos explotando un entorno de ‘XSS reflejado’ en AngularJS, donde no se permite el uso de cadenas, comillas, ni funciones como ‘**eval**‘. Reforzamos lo aprendido en la clase anterior y profundizamos en cómo manipular constructores y prototipos para ejecutar expresiones dentro del sandbox.

El foco está en utilizar estructuras internas del lenguaje para fabricar dinámicamente código válido sin recurrir a literales de texto. Se emplean métodos como ‘**toString()**‘, ‘**constructor**‘, y ‘**fromCharCode**‘ para construir instrucciones como ‘**alert(1)**‘ a partir de sus equivalentes en código numérico.

La clave del bypass sigue estando en redefinir el método ‘**charAt**‘ para interferir en el proceso de validación de AngularJS. Al combinar esto con filtros como ‘**orderBy**‘, conseguimos ejecutar código dentro de la plantilla sin activar las restricciones típicas del sandbox.

Esta clase cierra el bloque de técnicas avanzadas sobre AngularJS, mostrando cómo una comprensión profunda de JavaScript y el comportamiento de los frameworks puede permitir la ejecución de código incluso en entornos fuertemente limitados.

