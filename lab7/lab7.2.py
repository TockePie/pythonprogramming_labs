import os

subdir = "C:\\lab7\\Крадожон"

if not os.path.exists(subdir):
    os.makedirs(subdir)
    print(f"Підкаталог {subdir} успішно створено.")
else:
    print(f"Підкаталог {subdir} вже існує.")