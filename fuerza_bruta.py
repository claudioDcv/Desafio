import string

# todos los caracteres
all_chars = list(string.ascii_uppercase)

password = list(input('Ingrese contraseña de solo letras a decodificar\n'))

i = 0
intentos = 0

# iterar sobre la contraseña
while len(password) > i:
    # asignar indice a 0
    j = 0
    # se itera sobre lita de todas las letras mientras el indice 
    # sea menor al largo de la lista de caracteres
    while len(all_chars) > j:
        intentos += 1

        # se compara letra de contraseña con una de las letras en el listado de catacteres
        if password[i].upper() == all_chars[j]:
            break
        j += 1
    i += 1

print(intentos)