# A) Парні індекси
def elements_with_even_indices(lst):
    return lst[::2]
# B) Парні елементи
def even_elements(lst):
    ev_el = [el for el in lst if el % 2 == 0]
    return ev_el
# C) Більше попереднього
def more_than_previous_one(lst):
    elements_more = [lst[el] for el in range(1, len(lst)) if lst[el] > lst[el-1]]
    return elements_more
# D) Перший додатний
def first_positive_index(lst):
    index = 0
    while lst[index] <= 0:
        index += 1
    return index
# E) Перший додатний - 2
def first_positive_index_2(lst):
    index = 0
    while index < len(lst) and lst[index] <= 0:
        index += 1
    return index if index < len(lst) else -1
# F) Найбільший елемент
def max_value_and_index(lst):
    max_value = max(lst)
    max_index = lst.index(max_value)
    return max_value, max_index
# G) Більше своїх сусідів
def count_elements_greater_than_neighbors(lst):
    count = 0
    for el in range(1, len(lst) - 1):
        if lst[el] > lst[el - 1] and lst[el] > lst[el + 1]:
            count += 1
    return count
# H) Найменший додатний
def smallest_positive(lst):
    positive_num = [num for num in lst if num > 0]
    return min(positive_num)
# I) Найближче число
def closest_num(lst, x):
    min_diff = float('inf')
    closest_element = None
    for num in lst:
        diff = abs(num - x)
        if diff < min_diff:
            min_diff = diff
            closest_element = num
            if min_diff == 0:
                break
    return closest_element
# J) Шеренга
def line(lst, x):
    position = 1
    index = len(lst) - 1
    while index >= 0 and lst[index] < x:
        position += 1
        index -= 1
    return position
# K) Кількість різних елементів
def distinct_count(lst):
    dist_count = 1
    for i in range(1, len(lst)):
        if lst[i] != lst[i - 1]:
            dist_count += 1
    return dist_count
# L) Найменший непарний
def min_odd(lst):
    min = 0
    for i in range(len(lst)):
        if lst[i] % 2 == 1:
            min = lst[i]
            break
    for i in range(len(lst)):
        if lst[i] % 2 == 1:
            if lst[i] < min:
                min = lst[i]
    if min != 0:
        return min
    else:
        return 0
# M) Переставити в зворотньому порядку
def reverse_elements(lst):
    index_left = 0
    index_right = len(lst) - 1
    while index_left < index_right:
        lst[index_left], lst[index_right] = lst[index_right], lst[index_left]
        index_left += 1
        index_right -= 1
    return lst
# N) Переставити сусідні
def rearrange_adjacent_elements(lst):
    rearrange = []
    for i in range(0, len(lst) - 1, 2):
        rearrange.append(lst[i + 1])
        rearrange.append(lst[i])
    if len(lst) % 2 != 0:
        rearrange.append(lst[len(lst) - 1])
    return rearrange
# O) Переставити min i max
def rearrange_max_min(lst):
    min_index = lst.index(min(lst))
    max_index = lst.index(max(lst))
    lst[min_index], lst[max_index] = lst[max_index], lst[min_index]
    return lst
# R) Кількість співпадаючих пар
def matching_pairs(lst):
    pair_count = 0
    for a in range(len(lst)):
        for b in range(a + 1, len(lst)):
            if lst[a] == lst[b]:
                pair_count += 1
    return pair_count
# T) Кількість різних елементів - 2
def distinct_count_2(lst):
    count = 0
    for a in range(len(lst)):
        is_unique = True
        for b in range(a + 1, len(lst)):
            if lst[a] == lst[b]:
                is_unique = False
                break
        if is_unique:
            count += 1
    return count
# V) Унікальні елементи
def unique_elements(lst):
    for a in range(len(lst)):
        count = 0
        for b in range(len(lst)):
            if lst[a] == lst[b]:
                count += 1
        if count == 1:
            return lst[a]
