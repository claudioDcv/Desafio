n = int(input("Ingrese un número para comenzar la cuenta\n"))

# agregamos un valor inicial al rango quedando range(valor inicial, valor final)
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i)