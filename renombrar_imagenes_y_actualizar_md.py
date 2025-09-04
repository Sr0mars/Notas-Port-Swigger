import os
import re

# Carpeta donde están tus notas Markdown
notas_folder = "."  # la carpeta actual
# Carpeta donde están las imágenes
imagenes_folder = "Imagenes"

# Renombrar las imágenes reemplazando espacios por guiones bajos
for root, dirs, files in os.walk(imagenes_folder):
    for file in files:
        if " " in file:
            old_path = os.path.join(root, file)
            new_file = file.replace(" ", "_")
            new_path = os.path.join(root, new_file)
            os.rename(old_path, new_path)
            print(f"Renombrada: {file} -> {new_file}")

# Actualizar enlaces en los archivos Markdown
for root, dirs, files in os.walk(notas_folder):
    for file in files:
        if file.endswith(".md"):
            file_path = os.path.join(root, file)
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Reemplaza los enlaces de imágenes que tienen espacios
            def replacer(match):
                nombre = match.group(1)
                nuevo_nombre = nombre.replace(" ", "_")
                return f"![{nuevo_nombre}]({imagenes_folder}/{nuevo_nombre})"

            new_content = re.sub(r'!\[\[(.*?)\]\]', replacer, content)
            new_content = re.sub(r'!\[(.*?)\]\((.*?)\)', replacer, new_content)

            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Actualizados enlaces en: {file}")

print("¡Renombrado y actualización de enlaces completada!")
