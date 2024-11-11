"""
План работы:
1 Загрузить файл, прочитать его и сохранить текст в переменную text.

2.1 Удалить из текста знаки пунктуации и привести текст к одному регистру.
2.2 Разбить текст на слова,
2.3 Подсчитать количество уникальных слов.

3 Подсчитать количество гласных и согласных букв.

4

"""
from string import punctuation
#import nltk

#1 Загрузить файл, прочитать его и сохранить текст в переменную text.
with open("Eugene_Piuta/DZ_03/file1.txt", encoding='utf-8') as f:
    text = f.read()


#2.1 Удаление знаков пунктуации и цифр. Приводим текст в нижний регистр.

numbers = set(range(0, 10))
exclude = set(set(punctuation)|numbers)
# Добавим дополнительные знаки в исключения, т.к. они присутствует в тексте
exclude.add("…")
exclude.add("“")
exclude.add("”")
text = ''.join(ch for ch in text if ch not in exclude)
text = text.lower()
print(text)

#2.2 Разбиваем текст на слова.
words = text.split(" ")

#2.3 Подсчитать количество уникальных слов.
def find_words():    
    unique_words = set()
    for word in words:
        unique_words.add(word)
    n = len(unique_words)
    return(n)

print(f"Количество уникальных слов: {find_words()}")

# 3 Подсчитать количество гласных и согласных букв.

gls = "аеиоуюя"
gls_count = 0
for letter in gls:
     gls_count += text.count(letter)
sogl_count = len(text) - gls_count
print(f"Количество гласных букв в тексте: {gls_count}\n"
        f"Количество согласных букв в тексте: {sogl_count}")