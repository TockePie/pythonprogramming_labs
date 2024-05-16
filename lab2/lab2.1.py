from math import *

x = float(input("Введіть x: "))
y = float(input("Введіть y: "))
z = float(input("Введіть z: "))

F = (4 * x ** 3 + log(y, e)) / (e ** (z + y) + 7.2 * sin(y))

print("Відповідь: F дорівнює " + str(F))