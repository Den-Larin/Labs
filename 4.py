# Словники
# K) Номер появи слова
def count_previous(text):
    words = text.split()
    word_counts = {}
    previous_counts = []
    for word in words:
        if word not in word_counts:
            word_counts[word] = 0
        previous_counts.append(word_counts[word])
        word_counts[word] += 1
    return previous_counts
# L) Словник синонімів
def dict_of_synonims(n, words, given_word):
    synonyms = {}
    words_list = words.split()
    for i in range(0, 2*n, 2):
        word1, word2 = words_list[i], words_list[i + 1]
        synonyms[word1] = word2
        synonyms[word2] = word1
    synonym = synonyms.get(given_word)
    return synonym
# M) Вибори в США
def summary_of_election_results(data):
    candidates = {}
    data_list = data.split()
    for i in range(0, len(data_list), 2):
        candidate, count = data_list[i], data_list[i + 1]
        if candidate in candidates:
            candidates[candidate] += int(count)
        else:
            candidates[candidate] = int(count)
    return candidates
print(summary_of_election_results('McCain 10 McCain 5 Obama 9 Obama 8 McCain 1'))
# N) Найчастіше слово
def most_often_number(text):
    word_counts = {}
    words = text.split()
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    max_count = 0
    most_frequent_word = None
    for word, count in word_counts.items():
        if count > max_count or (count == max_count and (most_frequent_word is None or word < most_frequent_word)):
            most_frequent_word = word
            max_count = count
    return most_frequent_word
print(most_often_number('apple orange banana banana orange'))
# P) Частотний аналіз
def sort_words(text):
    word_counts = {}
    words = text.split()
# Q) Країни та міста
# R) Банківські рахунки
# S) Контрольна по наголосам
# T) Продажі
# V) Вибори в США - 2
# O) Права доступу
# Множини
# A) Кількість різних чисел
# B) Кількість співпадаючих
# C) Перетин списків
# D) Чи зустрічалось число раніше
# E) Кубики
# F) Кількість слів в тексті
# G) Вгадай число
# H) Вгадай число - 2
# I) Поліглоти
# J) Страйки
