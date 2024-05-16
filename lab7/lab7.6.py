import re

# Визначаємо клас для обробки файлів
class FileProcessor:

    # Конструктор класу, приймає назву вхідного файлу
    def __init__(self, input_file):
        self.input_file = input_file

    # Метод для зчитування тексту з файлу
    def read_text(self):
        with open(self.input_file, "r", encoding="utf-8") as f:
            text = f.read()
        return text

    # Метод для розбиття тексту на речення
    def split_sentences(self, text):
        # Використовуємо регулярний вираз для пошуку крапок, знаків оклику та питання
        sentences = re.split(r"[.!?]\s+", text)
        return sentences

    # Метод для розбиття речення на слова
    def split_words(self, sentence):
        # Використовуємо регулярний вираз для пошуку слів, що складаються з букв
        words = re.findall(r"\w+", sentence)
        return words

    # Метод для обчислення середньої кількості слів у реченнях
    def average_words(self, sentences):
        total_words = 0
        for sentence in sentences:
            # Розбиваємо речення на слова
            words = self.split_words(sentence)
            total_words += len(words)
        average = total_words / len(sentences)
        return average

    # Метод для створення файлу з реченнями, кількість слів у яких найближча до середньої
    def create_file_161(self, sentences, average):
        # Відкриваємо файл для запису
        with open("161.txt", "w", encoding="utf-8") as f:
            for sentence in sentences:
                # Розбиваємо речення на слова
                words = self.split_words(sentence)
                if abs(len(words) - average) <= 1:
                    # Записуємо речення в файл з крапкою в кінці
                    f.write(sentence + ".\n")

    # Метод для створення файлу з кириличними буквами, що замінені на букви в реверсному порядку алфавіту
    def create_file_162(self, text):
        # Визначаємо кириличний алфавіт в нижньому регістрі
        alphabet = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
        # Визначаємо реверсний алфавіт в нижньому регістрі
        reverse = alphabet[::-1]
        substitution = dict(zip(alphabet, reverse))
        modified_text = ""
        for char in text:
            # Якщо символ є кириличною буквою в нижньому регістрі
            if char in alphabet:
                # Замінюємо його на відповідну букву з реверсного алфавіту
                modified_text += substitution[char]
            # Якщо символ є кириличною буквою в верхньому регістрі
            elif char.lower() in alphabet:
                # Замінюємо його на відповідну букву з реверсного алфавіту в верхньому регістрі
                modified_text += substitution[char.lower()].upper()
            else:
                # Залишаємо символ без змін
                modified_text += char
        # Відкриваємо файл для запису
        with open("162.txt", "w", encoding="utf-8") as f:
            f.write(modified_text)

# Створюємо об'єкт класу FileProcessor з назвою вхідного файлу
fp = FileProcessor("16.txt")
text = fp.read_text()
sentences = fp.split_sentences(text)
# Обчислюємо середню кількість слів у реченнях
average = fp.average_words(sentences)
fp.create_file_161(sentences, average)
fp.create_file_162(text)