import string
# todos los caracteres
all_chars = string.ascii_uppercase
# dejamos todo en mayuscula para ignorar CASE

original_pass = input('Ingrese contraseña de solo letras a decodificar\n')
password = original_pass.upper()
intentos = 0

for letra_a_descifrar in password:
    for texto_a_comparar in all_chars:
        intentos += 1
        if letra_a_descifrar == texto_a_comparar:
            # si la comparacion ha sido correcta, salimos del ciclo interno y probamos la siguiente letra
            break
print('Ingresa contraseña {}\n{} intentos\n'.format(original_pass, intentos))