import string

# todos los caracteres
all_chars = string.ascii_uppercase
password = input('Ingrese contraseña de solo letras a decodificar\n')
intentos = 0


for l in password:
    for t in all_chars:
        intentos += 1
        if l.upper() == t:
            break
print(intentos)