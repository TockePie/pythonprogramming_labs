class Countries:
    def __init__(self, data):
        # Словник з державами та кортежами з назвою столиці, її площею та чисельністю населення
        self.data = data

    # Метод, який повертає список держав, столиці яких мають чисельність населення в заданому діапазоні
    def get_countries_by_population(self, min_pop, max_pop):
        result = []
        for country, (capital, area, population) in self.data.items():
            if min_pop <= population <= max_pop:
                # Додаємо до результату кортеж з назвою держави, столиці, площі та населення
                result.append((country, capital, area, population))
        # Сортуємо результат за спаданням населення столиці
        result.sort(key=lambda x: x[3], reverse=True)
        return result

    # Метод, який повертає список держав, які мають столиці з заданим діапазоном площі
    def get_countries_by_area(self, min_area, max_area):
        result = []
        for country, (capital, area, population) in self.data.items():
            if min_area <= area <= max_area:
                result.append((country, capital, area, population))
        result.sort(key=lambda x: x[2], reverse=True)
        return result

    # Метод, який повертає відношення площі столиці до площі держави
    def get_area_ratio(self, country):
        if country in self.data:
            capital, area, population = self.data[country]
            # Отримуємо площу держави з Вікіпедії за допомогою функції search_web
            query = country + " площа"
            results = search_web(query)
            if results:
                # Беремо перший результат та його сніпет
                result = results["web_search_results"][0]
                snippet = result["snippet"]
                # Знаходимо площу держави в сніпеті за допомогою регулярного виразу
                import re
                pattern = r"(\d+(?:[.,]\d+)?)\s*(км²|га)"
                match = re.search(pattern, snippet)
                if match:
                    # Отримуємо значення та одиницю виміру
                    value = float(match.group(1).replace(",", "."))
                    unit = match.group(2)
                    # Переводимо площу держави в квадратні кілометри
                    if unit == "га":
                        value = value / 100
                    # Обчислюємо відношення площі столиці до площі держави
                    ratio = area / value
                    return ratio
        # Якщо держави немає в наших даних
        return None

    # Метод, який повертає назву держави, до якої належить столиця
    def get_country_by_capital(self, capital):
        for country, (cap, area, population) in self.data.items():
            if cap == capital:
                return country
        return None

# Створюємо об'єкт класу з даними про деякі держави та їх столиці
# Дані про столиці взяті з Вікіпедії
countries = Countries({
    "Україна": ("Київ", 839, 2966000),
    "Франція": ("Париж", 105.4, 2148000),
    "Німеччина": ("Берлін", 891.8, 3600000),
    "Італія": ("Рим", 1285, 2873000),
    "Іспанія": ("Мадрид", 604.3, 3223000),
    "Польща": ("Варшава", 517.2, 1790000),
    "США": ("Вашингтон", 177, 705749),
    "Канада": ("Оттава", 2778, 934243),
    "Китай": ("Пекін", 16410.54, 21540000),
    "Японія": ("Токіо", 2187.66, 13929286),
    "Індія": ("Нью-Делі", 42.7, 257803),
    "Бразилія": ("Бразилія", 5802, 3015268),
    "Австралія": ("Канберра", 814.2, 397393)
})

min_pop = int(input("Введіть мінімальну чисельність населення столиць: "))
max_pop = int(input("Введіть максимальну чисельність населення столиць: "))

countries_by_population = countries.get_countries_by_population(min_pop, max_pop)

# Виводимо список держав, столиці, площі та населення столиць: Якщо список не порожній
if countries_by_population:
    print(f"Список держав, столиці яких мають чисельність населення в діапазоні від {min_pop} до {max_pop} осіб: ")
    print("| Держава | Столиця | Площа, км² | Населення, осіб |")
    print("| ------- | ------- | --------- | -------------- |")
    for country, capital, area, population in countries_by_population:
        print(f"| {country} | {capital} | {area} | {population} |")
else:
    print(f"Немає держав, столиці яких мають чисельність населення в діапазоні від {min_pop} до {max_pop} осіб.")