import numpy as np

try:
    #Користувач вводить дані
    m = input("Дано: Матриця MxM, де m > 1:\nm = ")
    minNum = input("Введіть мінімальне ціле значення числа у матриці: ")
    maxNum = input("І введіть максимальне ціле значення: ")

    # Перевіряємо, чи користувач щось ввів
    if minNum == "" or maxNum == "" or m == "":
        raise ValueError("Ви не ввели один, два або жодного значення")

    #Перетворюємо рядки на цілі числа
    minNum = int(minNum)
    maxNum = int(maxNum)
    m = int(m)

    #Перевіряємо, чи maxNum більший за minNum
    if maxNum < minNum:
       raise ValueError("Максимальне значення повинно бути більшим за мінімальне")

    #Перевіряємо, чи матриця більша за 1
    if m <= 1:
        raise ValueError("Розмір матриці повинний бути більшим за 1")

    #Генеруємо квадратну матрицю A(m,m)
    A = np.random.randint(minNum, maxNum, (m, m))

    #Виводимо початкову матрицю A
    print("Початкова матриця A: \n{}".format(A))

    #Сортуємо рядки матриці A за спаданням елементів
    A_sorted = np.sort(A, axis=1)[:, ::-1]

    #Транспонуємо матрицю A_sorted, щоб отримати нову матрицю B, стовпцями якої будуть упорядковані рядки A
    B = A_sorted.T

    # виводимо нову матрицю B
    print("Нова матриця B: \n{}".format(B))

except ValueError as text_of_error:
    #Виводимо повідомлення про помилку
    print("\nПомилка: {}".format(text_of_error))