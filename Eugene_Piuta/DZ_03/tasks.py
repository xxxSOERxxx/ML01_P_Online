"""
План работы:
1 Загрузить файл, прочитать его и сохранить текст в переменную text.

2.1 Удалить из текста знаки пунктуации и привести текст к одному регистру.
2.2 Разбить текст на слова,
2.3 Подсчитать количество уникальных слов.

3 Подсчитать количество гласных и согласных букв.

4.

"""
from string import punctuation
import nltk, copy

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
text_new =copy.copy(text)
text_new = ''.join(ch for ch in text_new if ch not in exclude)
text_new = text_new.lower()
print(text_new)

#2.2 Разбиваем текст на слова.
words = text_new.split(" ")

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
     gls_count += text_new.count(letter)
sogl_count = len(text_new) - gls_count
print(f"Количество гласных букв в тексте: {gls_count}\n"
        f"Количество согласных букв в тексте: {sogl_count}")

# 4.1 Находим количество предложений с помощью nltk
from nltk.tokenize import sent_tokenize
#nltk.download("stopwords")
#nltk.download('punkt_tab')
sentences = sent_tokenize(text, language="russian")
print((f"Количество предложений в тексте: {len(sentences)}"))
print(text)
print(sentences)