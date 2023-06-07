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
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    word_tuples = [(count, word) for word, count in word_counts.items()]
    sorted_words = sorted(word_tuples, key=lambda x: (-x[0], x[1]))
    sorted_words_list = [word for count, word in sorted_words]
    return sorted_words_list
print(sort_words('hi hi what is your name my name is bond james bond my name is damme van damme claude van damme jean claude van damme'))
# Q) Країни та міста
countries = {}
n = int(input())
for i in range(n):
    country_cities = input().split()
    country = country_cities[0]
    cities = country_cities[1:]
    countries[country] = cities
m = int(input())
for i in range(m):
    city = input()
    for country, cities in countries.items():
        if city in cities:
            print(country)
# R) Банківські рахунки

accounts = {}

def deposit(accounts, name, sum):
    if name not in accounts:
        accounts[name] = 0
    accounts[name] += sum

def withdraw(accounts, name, sum):
    if name not in accounts:
        accounts[name] = 0
    accounts[name] -= sum

def balance(accounts, name):
    if name not in accounts:
        return "ERROR"
    return accounts[name]

def transfer(accounts, name1, name2, sum):
    if name1 not in accounts:
        accounts[name1] = 0
    if name2 not in accounts:
        accounts[name2] = 0
    accounts[name1] -= sum
    accounts[name2] += sum

def income(accounts, p):
    for name, balance in accounts.items():
        if balance > 0:
            accounts[name] += int(balance * p / 100)

while True:
    command = input().split()
    if command[0] == "DEPOSIT":
        deposit(accounts, command[1], int(command[2]))
    elif command[0] == "WITHDRAW":
        withdraw(accounts, command[1], int(command[2]))
    elif command[0] == "BALANCE":
        print(balance(accounts, command[1]))
    elif command[0] == "TRANSFER":
        transfer(accounts, command[1], command[2], int(command[3]))
    elif command[0] == "INCOME":
        income(accounts, int(command[1]))
    elif command[0] == "Exit":
        break
# S) Контрольна по наголосам
n = int(input())
dictionary = {}
for i in range(n):
    word = input()
    base_form = word.lower()
    if base_form not in dictionary:
        dictionary[base_form] = set()
    dictionary[base_form].add(word)
errors = 0
exercise = input().split()
for word in exercise:
    base_form = word.lower()
    if (base_form in dictionary and word not in dictionary[base_form] or len([letter for letter in word if letter.isupper()]) != 1):
        errors += 1
print(errors)
# T) Продажі
sales_dict = {}

while True:
    line = input()
    if not line:
        break
    customer, purchase, count = line.split()
    if customer not in sales_dict:
        sales_dict[customer] = {}
    sales_dict[customer][purchase] = sales_dict[customer].get(purchase, 0) + int(count)

for customer, purchases in sorted(sales_dict.items()):
    print(customer + ':')
    for purchase, count in sorted(purchases.items()):
        print(purchase, count)
# V) Вибори в США - 2
votes = {}
num_states = int(input())
for i in range(num_states):
    state, count = input().split()
    votes[state] = [{}, int(count)]

results = {}
while True:
    vote = input().split()
    if not vote:
        break
    state, candidate = vote
    votes[state][0][candidate] = votes[state][0].get(candidate, 0) + 1
    results[candidate] = 0

for key in votes:
    winner = ('', 0)
    for candidate in votes[key][0]:
        if votes[key][0][candidate] > winner[1]:
            winner = (candidate, votes[key][0][candidate])
        elif votes[key][0][candidate] == winner[1] and candidate < winner[0]:
            winner = (candidate, votes[key][0][candidate])
    results[winner[0]] += votes[key][1]

sorted_results = sorted(results.items(), key=lambda item: (-item[1], item[0]))
for candidate, count in sorted_results:
    print(candidate, count)
# O) Права доступу
permissions = {}
n = int(input())
for i in range(n):
    items = input().split()
    permissions[items[0]] = set(items[1:])
m = int(input())
for i in range(m):
    operation, file = input().split()
    if operation == 'read':
        operation = 'R'
    if operation == 'write':
        operation = 'W'
    if operation == 'execute':
        operation = 'X'
    if operation in permissions[file]:
        print('OK')
    else:
        print('Access denied')
