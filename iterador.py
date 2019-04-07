# cuenta_regresiva = int(input("Ingrese un número para comenzar la cuenta\n"))

print('WHILE:\n')

i = 0
while i < 50:
    print("Iteración {}".format(i + 1))
    i +=1

'''
EXPLICACIÓN
i = numero inicial
Mientras i sea menor a 50(que llamaremos n) Repetir
    codigo a repetir
    i aumentar en uno
'''

# while, conversión a for
print('----------------------------------------------------\n')
print('FOR:\n')

for i in range(50):
    print("Iteración {}".format(i + 1))


'''
EXPLICACIÓN
- range toma un numero y crea una lista desde el 0 hasta el numero indicado como argumento
- aqui el numero es cincuenta, por lo tanto se genera una lista [0,1,2,3,4,5...,49,50]
- for se repetira tantas veces como numeros tenga la lista

numero 50 que llemaremos n
Para i(numero entero) en el rango de 0 hasta numero n
    codigo a repetir
'''