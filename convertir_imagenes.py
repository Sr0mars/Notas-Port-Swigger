import os
import re

# Carpeta donde están tus notas
notas_folder = "."

# Carpeta donde están tus imágenes
imagenes_folder = "imagenes"

# Buscar todos los archivos .md
for root, dirs, files in os.walk(notas_folder):
    for file in files:
        if file.endswith(".md"):
            file_path = os.path.join(root, file)
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Reemplazar ![[Archivo.png]] por ![Archivo](imagenes/Archivo.png)
            def replacer(match):
                nombre = match.group(1)
                return f"![{nombre}]({imagenes_folder}/{nombre})"

            new_content = re.sub(r'!\[\[(.*?)\]\]', replacer, content)

            # Guardar cambios
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)

print("¡Enlaces de imágenes actualizados correctamente!")
