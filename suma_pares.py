from functools import reduce

n = int(input("Ingrese un número para comenzar la cuenta\n"))

total = 0
for i in range(n + 1):
    if i % 2 == 0:
        total += i

print(total)