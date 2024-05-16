#Задано список
capitals = {"Київ": 3133712, "Варшава": 1863056, "Прага": 1179384,
        "Братислава": 424428, "Кишинів": 532513, "Бухарест": 1926334}

try:
    minNum = input("Введіть мінімальну кількість жителів: ")
    maxNum = input("і максимальну: ")

    #Якщо якесь значення порожнє, то користувач отримає помилку
    if minNum == "" or maxNum == "":
        raise ValueError("Введений рядок порожній!")

    #Так само, якщо значення буде не натуральним числом
    if not minNum.isdigit() and maxNum.isdigit():
        raise ValueError("Ви повинні ввести натуральні числа")
    minNum = int(minNum)
    maxNum = int(maxNum)

    #Або коли мінімальне значення буде більше
    if minNum > maxNum:
        raise ValueError("Мінімальне значення жителів перевищує максимальне!")

    #Створюємо порожній список. Якщо населення міста знаходиться в діапазоні, додаймо його і його населення до списку
    cities = []
    for city, population in capitals.items():
        if minNum <= population <= maxNum:
            cities.append((city, population))

    #Виводимо результат із форматуванням
    print("\nМіста і їх населення, які відповідають введеному діапазону:")
    for city, population in cities:
        print(f"{city} - {population} мільйонів")

#А якщо у нас виникне помилка, то ми будемо знати чому
except ValueError as text_of_error:
    print(f"\nПомилка: {text_of_error}")
    exit()