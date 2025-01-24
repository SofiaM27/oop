import re
from collections import Counter

def parse_text(file_path):
    """Зчитує текстовий файл і повертає список слів без спеціальних символів."""
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().lower()
    words = re.findall(r'\b\w+\b', text)  # Вилучення лише слів
    return words

def count_word_frequencies(words):
    """Підраховує частоту слів у списку."""
    return Counter(words)

def count_word_frequencies(words):
    """Підраховує частоту слів у списку."""
    return Counter(words)

def print_sorted_frequencies(word_counts):
    """Виводить список слів, відсортований за частотою вживання."""
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    for word, count in sorted_words:
        print(f"{word}: {count}")

if __name__ == "__main__":
    file_path = "Доповідь фізика.docx"  # Змінити на шлях до файлу
    words = parse_text(file_path)
    word_counts = count_word_frequencies(words)
    print_sorted_frequencies(word_counts)
