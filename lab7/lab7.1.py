import os

path = "C:\\"
name = "lab7"

# Створюємо повний шлях до каталогу
full_path = os.path.join(path, name)

if os.path.exists(full_path):
    print(f"Каталог {full_path} вже існує.")
else:
    os.mkdir(full_path) #Створюється каталог
    print(f"Каталог {full_path} успішно створено.")