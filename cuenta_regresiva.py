print('FOR:\n')

cuenta_regresiva = int(input("Ingrese un número para comenzar la cuenta\n"))

for i in range(cuenta_regresiva):
    tmp = cuenta_regresiva
    print("Iteración {}".format(tmp - i))


# for, conversión a while

print('----------------------------------------------------\n')
print('WHILE:\n')

cuenta_regresiva = int(input("Ingrese un número para comenzar la cuenta\n"))

tmp = cuenta_regresiva
while 0 < tmp:
    print("Iteración {}".format(tmp))
    tmp -= 1