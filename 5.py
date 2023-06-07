# Множини
# A) Кількість різних чисел
print(len(set(input().split())))
# B) Кількість співпадаючих
print(len(set(input().split()).intersection(set(input().split()))))
# C) Перетин списків
print(sorted(set(input().split()) & set(input().split())))
# D) Чи зустрічалось число раніше
numbers = set()
for i in input().split():
    if i not in numbers:
        numbers.add(i)
        print('NO')
    else:
        print('YES')
# E) Кубики
n, m = [int(i) for i in input().split()]
ir = set()
ig = set()
for i in range(n):
    ir.add(int(input()))
for i in range(m):
    ig.add(int(input()))
print(len(ir & ig))
print(sorted(ir & ig))
print(len(ir - ig))
print(sorted(ir - ig))
print(len(ig - ir))
print(sorted(ig - ir))
# F) Кількість слів в тексті
with open('input.txt', 'r') as file:
    text = file.read()
words = text.split()
different_words = set(words)
num_different_words = len(different_words)
print(num_different_words)
# G) Вгадай число
n = int(input())
all_nums = set(range(1, n + 1))
possible_nums = all_nums
while True:
    num = input()
    if num == 'HELP':
        break
    num = {int(i) for i in num.split()}
    answer = input()
    if answer == 'YES':
        possible_nums &= num
    elif answer == 'NO':
        possible_nums &= all_nums - num
print(' '.join([str(i) for i in sorted(possible_nums)]))
# H) Вгадай число - 2
n = int(input())
all_nums = set(range(1, n + 1))
possible_nums = all_nums
while True:
    num = input()
    if num == 'HELP':
        break
    num = {int(i) for i in num.split()}
    if len(possible_nums & num) > len(possible_nums) / 2:
        print('YES')
        possible_nums &= num
    else:
        print('NO')
        possible_nums &= all_nums - num
print(' '.join([str(i) for i in sorted(possible_nums)]))
# I) Поліглоти
n = int(input())
language = []
for i in range(n):
    mi = int(input())
    s = set()
    for i in range(mi):
        s.add(input())
    language.append(s)
known_by_everyone = set.intersection(*language)
known_by_someone = set.union(*language)
print(len(known_by_everyone), '\n'.join(known_by_everyone), len(known_by_someone), '\n'.join(known_by_someone), sep='\n')
# J) Страйки
n, k = [int(i) for i in input().split()]
strikes = [[int(i) for i in input().split()] for i in range(k)]
strike_days = set()
for i in range(k):
    for j in range(strikes[i][0], n + 1, strikes[i][1]):
        if j % 7 != 0 and j % 7 != 6:
            strike_days.add(j)
print(len(strike_days))
