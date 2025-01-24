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
