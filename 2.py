# Вправа 1:
names = ['Max', 'Tatiana', 'Vitaliy', 'Sophia', 'Anastasia']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
# Вправа 2:
types_of_transport = ['велосипед', 'автомобіль', 'тролейбус']
print(f'Я хотів би купити {types_of_transport[0]}')
print(f'Я мрію купити {types_of_transport[1]}')
print(f'Зазвичай я їжджу на {types_of_transport[2]}і')
# Вправа 3:
years_list = [2005, 2006, 2007, 2008, 2009, 2010]
print(f'У {years_list[3]} році мені виповнилося 3 роки')
years_list.append(2011)
print(years_list)
print(f'Найбільше років було у {years_list[-1]} році')
# Вправа 4:
things = ['wallet', 'mirror', 'umbrella']
print(things[2].capitalize())
print(things)
things[2] = things[2].upper()
print(things)
things.remove(things[2])
print(things)
# Вправа 5:
languages = ['Georgian', 'Estonian', 'Ukrainian']
print(languages[-1].lower())
languages[-1] = languages[-1][::-1].capitalize()
print(languages[-1])
# Вправа 6:
hardware = ('monitor', 'web browser', 'keyboard')
software = ['search', 'printer', 'operating system']
for i in hardware:
    print(i)
for i in software:
    print(i)
software[1] = 'CPU'
print(software)
# Висновок: у списку можливо замінити елемент, у кортежі - ні.
# Задача 1:
languages = ['Ukrainian', 'French', 'Bulgarian', 'Norwegian', 'Latvian']
languages = sorted(languages)
print(languages)
languages.reverse()
print(languages)
languages.sort()
print(languages)
# Задача 2:
numbers = input().split()
sum = 0
for i in numbers:
    sum += int(i)
print(sum)
# Задача 3:
cities = ['Budapest', 'Rome', 'Istanbul', 'Sydney', 'Kyiv', 'Hong Kong']
message = ', '.join(cities[:-1]) + ' and ' + cities[-1]
print(message)
# Задача 4:
digits = input().split()
list_reverse = sorted(digits, reverse=True)
number = int(''.join(list_reverse))
print(number)
# Задача 5:
oceans = ['Pacific Ocean', 'Arctic Ocean', 'Indian Ocean', 'Atlantic Ocean']
oceans_copy = list(oceans)
print(oceans_copy)
print(len(oceans))
print(list('oceans'))
print(', '.join(oceans))
print(oceans.index('Indian Ocean'))
oceans.append('Southern Ocean')
print(oceans)
oceans.insert(6, 'Non-existent Ocean')
print(oceans)
del oceans[-1]
print(oceans)
sorted_oceans = sorted(oceans)
print(sorted_oceans)
oceans.reverse()
print(oceans)
# Задача 6:
keywords = ('for', 'if', 'else', 'in', ':')
print(f'{keywords[0]} each token {keywords[3]} the postfix expression {keywords[-1]}')
print(f'{keywords[1].rjust(6)} the token is a number {keywords[-1]}')
print(f'print('"'Convert it to an integer and add it to the end of values'"')'.rjust(73))
print(f'{keywords[2].rjust(8)} {keywords[-1]}')
print(f'print('"'Append the result to the end of values'"')'.rjust(55))
