# Вправа 1:
print(60 * 60)
# Вправа 2:
seconds_per_hour = 60 * 60
print(seconds_per_hour)
# Вправа 3:
print(seconds_per_hour * 24)
# Вправа 4:
seconds_per_day = seconds_per_hour * 24
print(seconds_per_day)
# Вправа 5:
dp = seconds_per_day / seconds_per_hour
print(dp)
# Вправа 6:
d = seconds_per_day // seconds_per_hour  # результат збігається
print(d)
# Вправа 7:
print(8 + 4)
print(15 - 3)
print(3 * 4)
print(36 // 3)
# Вправа 8:
a = 12
print(f'Моє улюблене число: {a}')
# Вправа 9:
name = "Denys"
print(name.upper())
print(name.lower())
print(name.swapcase())
# Вправа 10:
poem = '''Yes, I'll smile, indeed, through tears and weeping
Sing my songs where evil holds its sway,
Hopeless, a steadfast hope forever keeping,
I shall live! You thoughts of grief, away!'''
print(poem[:15])
print(len(poem))
print(poem.startswith('Yes'))
print(poem.endswith('I shall live!'))
print(poem.find(','))
print(poem.rfind(','))
print(poem.count(','))
print(poem.isalnum())
# Задача 1:
gr = 'Hello, World!'
print(gr)
gr = 'Hi, I`m Den.'
print(gr)
# Задача 2:
your_name = 'Anastasia'
print('Hello,', your_name + ',', 'would you like to eat something?')
# Задача 3:
famous_person = 'Confucius'
message = '"What you do not wish for yourself, do not do to others."'
print(famous_person, 'once said,', message)
# Задача 4:
my_name = '   \tDenys\n   '
print(my_name.lstrip())
print(my_name.rstrip())
print(my_name.strip())
# Задача 5:
print('Name: Denys Larin')
print('Country: Ukraine')
print('Index: 58012')
print('City: Chernivtsi')
print('Street: Heroyiv Maydanu')
print('House number: 12')
# Задача 6:
distance = float(input('Введіть відстань (у метрах): '))
distance1 = 'Відстань (у дюймах): {d:.2f}'
print(distance1.format(d = distance * 39.370))
distance2 = 'Відстань (у футах): {d:.2f}'
print(distance2.format(d = distance * 3.2808))
distance3 = 'Відстань (у милях): {d:.2f}'
print(distance3.format(d = distance * 0.00062137))
distance4 = 'Відстань (у ярдах): {d:.2f}'
print(distance4.format(d = distance * 1.0936))
# Задача 7:
tr = int(input('Введіть тривалість події (у днях): '))
h = tr*24
m = h*60
s = m*60
print('{0:<10d} {1:<10d} {2:<10d}'.format(h, m, s))
# Задача 8:
c = float(input('Введіть значення температури у градусах Цельсія (С): '))
f = 32 + 9/5 * c
k = c + 273.15
print(f'Температура у градусах Фаренгейта(F): {f:^15.2f}')
print(f'Температура у градусах Кельвіна(K): {k:^15.2f}')
# Задача 9:
ch = int(input('Введіть чотирицифрове ціле число: '))
fch = ch // 1000
sch = (ch % 1000)//100
tch = (ch % 100)//10
frch = ch % 10
summ = fch + sch + tch + frch
print(f'{fch} + {sch} + {tch} + {frch} = {summ}')
# Задача 10:
import math
x1 = float(input())
x1 = math.radians(x1)
x2 = float(input())
x2 = math.radians(x2)
y1 = float(input())
y1 = math.radians(y1)
y2 = float(input())
y2 = math.radians(y2)
s = 6371.032 * math.acos(math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2))
print(f'{s:>10.3f}')
