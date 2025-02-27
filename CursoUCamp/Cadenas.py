import random

numero = random.randint(1,10)

x= "Python"

print(x[0])
print(x[5])
print(x[-1])
print(x[-6])
print(x[6])
print(x[-7])

x[0] = "p" # Los string son inmutables
x1 = "p" + x[1:]
print(x1)