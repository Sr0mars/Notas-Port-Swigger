En esta segunda parte exploramos cómo DOM Invader identifica gadgets en bibliotecas de terceros que han sido minificadas, lo cual dificulta su análisis manual. Realizamos un escaneo de gadgets sobre la base de los vectores encontrados previamente y descubrimos que se puede alcanzar un sink crítico: la función ‘**setTimeout**‘ a través de la propiedad ‘**hitCallback**‘.

Este tipo de gadgets permiten ejecutar código arbitrario al combinarse con la contaminación del prototipo. Gracias a la automatización de DOM Invader, obtenemos una prueba de concepto funcional con un simple alert(1). Esta clase pone en evidencia lo útil que es contar con herramientas de análisis dinámico frente a código ofuscado o minimizado.

Solucion
manualmente seria asi
Object.defineProperty(Object.prototype, 'YOUR-PROPERTY', {
    get() {
        console.trace();
        return 'polluted';
    }
})

Como lo hacemos manualmente
nos vamos al BS en proxysetting 
nos aseguramos que este palomeada
![[Pasted image 20250831234148.png]]
y ahora vamos a interceptar a la raiz le damos forward y veremos que nos sale el codigo en la otra respuesta
![[Pasted image 20250831234302.png]]
de tal menera que quedaria asi
<script>

    debugger;

</script>
![[Pasted image 20250831234450.png]]
le damos forward
y en consola le pegamos esto
Object.defineProperty(Object.prototype, 'hitCallback', {
    get() {
        console.trace();
        return 'polluted';
    }
})


