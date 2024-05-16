from math import sqrt

x = float(input("Введіть x: "))
y = float(input("Введіть y: "))

r1 = float(input("Введіть радіус першого кола: "))
r2 = float(input("Введіть радіус другого кола: "))

lenght = sqrt(x ** 2 + y ** 2)

if r1 < lenght < r2 or r2 < lenght < r1:
    print("Точка A(" +str(x)+ "," +str(y)+ ") знаходться всередині тора")

else:
    print("Точка A(" +str(x)+ "," +str(y)+ ") не знаходиться всередині тора")