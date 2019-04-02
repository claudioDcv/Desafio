n = int(input("Ingrese un número para comenzar la cuenta\n"))

# range crea una lista desde 0 hasta n - 1
# se aumenta en 1 el valor n para considerarlo dentro de las repeticiones (iteraciones)
for i in range(n + 1):
    if i % 2 == 0:
        print(i)