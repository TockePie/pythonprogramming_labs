import os
import shutil
import pickle

capitals = {"Київ": 3133712, "Варшава": 1863056, "Прага": 1179384,
        "Братислава": 424428, "Кишинів": 532513, "Бухарест": 1926334}

# Відкриваємо файл для запису в бінарному режимі
with open("capitals.pkl", "wb") as f:
    # Зберігаємо словник у файл за допомогою модуля pickle
    pickle.dump(capitals, f)

destination_path = "C:\\lab5\\"
shutil.move("capitals.pkl", destination_path)

# Відкриваємо файл для читання в бінарному режимі
with open(destination_path + "capitals.pkl", "rb") as f:
    # Зчитуємо словник з файлу за допомогою модуля pickle
    capitals = pickle.load(f)

# Доповнюємо словник новими даними
capitals["Берлін"] = 3644826
capitals["Париж"] = 2140526

with open(destination_path + "capitals_new.pkl", "wb") as f:
    pickle.dump(capitals, f)